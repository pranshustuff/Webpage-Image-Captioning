from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from processor.html_parser import process_html

app = FastAPI(title="Expanded HTML Image Captioning Assistant")

@app.post("/caption-html")
async def caption_html(
    html_files: list[UploadFile] = File(...),
    use_section_summary: bool = Form(False)
):
    """
    Accept multiple HTML files.
    Returns JSON with structured captions, section summaries, and enhanced HTML.
    """
  
    results = []

    for html_file in html_files:
        content = await html_file.read()
        modified_html, images_info, sections_info = process_html(
            content.decode("utf-8"), use_section_summary
        )
        results.append({
            "file": html_file.filename,
            "enhanced_html": modified_html,
            "images": images_info,
            "sections": sections_info if use_section_summary else None
        })

    return JSONResponse(content={"results": results})
