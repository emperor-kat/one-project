#!/usr/bin/env python3
import yaml
from datetime import datetime, timedelta

def check():
    with open('metadata_report.yml', 'r') as f:
        articles = yaml.safe_load(f) or []
    
    outdated = []
    for article in articles:
        last_checked = datetime.strptime(article['last_checked'], '%Y-%m-%d')
        if (datetime.now() - last_checked).days > 180:
            outdated.append(article)
    
    if outdated:
        print("Нужно обновить:")
        for article in outdated:
            print(f" - {article['title']} (ID: {article['id']})")
    else:
        print("Всё актуально!")

if __name__ == '__main__':
    check()