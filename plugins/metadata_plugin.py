from mkdocs.plugins import BasePlugin
import yaml
from datetime import datetime

class MetadataPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        if hasattr(page, 'meta') and page.meta:
            page.id = page.meta.get('id', '')
            page.update_frequency = page.meta.get('update_frequency', '')
        return markdown
    
    def on_post_build(self, config):
        report = []
        for page in config['pages']:
            if hasattr(page, 'id') and page.id:
                report.append({
                    'id': page.id,
                    'title': page.title,
                    'url': page.url,
                    'update_frequency': getattr(page, 'update_frequency', ''),
                    'last_checked': datetime.now().strftime('%Y-%m-%d')
                })
        
        with open('metadata_report.yml', 'w') as f:
            yaml.dump(report, f)