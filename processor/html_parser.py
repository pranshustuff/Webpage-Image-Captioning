from bs4 import BeautifulSoup
from .image_caption import caption_image_from_url
from .section_summary import summarize_text

def process_html(html_content: str, use_section_summary=False):
    soup = BeautifulSoup(html_content, "html.parser")
    images_info = []
    sections_info = []

    for img_tag in soup.find_all("img"):
        img_url = img_tag.get("src")
        if img_url:
            caption = caption_image_from_url(img_url)
            figure_tag = soup.new_tag("figure")
            img_tag.wrap(figure_tag)
            figcaption_tag = soup.new_tag("figcaption")
            figcaption_tag.string = caption
            img_tag.insert_after(figcaption_tag)
            images_info.append({"url": img_url, "caption": caption})

    if use_section_summary:
        for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
            section_text = heading.get_text(strip=True)
            content_texts = []
            for sibling in heading.find_next_siblings():
                if sibling.name and sibling.name.startswith("h"):
                    break
                content_texts.append(sibling.get_text(strip=True))
            full_text = "\n".join([section_text] + content_texts)
            summary = summarize_text(full_text)
            section_images = [img for img in images_info if img["url"] in full_text]
            sections_info.append({
                "heading": section_text,
                "summary": summary,
                "images": section_images
            })

    return str(soup), images_info, sections_info
