from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import json,xml.etree.ElementTree as ET
repo=Path(__file__).resolve().parents[1];c=json.loads((repo/'site-content.json').read_text());root=repo/c['root'];base=c['base'];prefix=urlparse(base).path
class P(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.ld=[];self.inld=False
 def handle_starttag(self,t,a):
  d=dict(a);self.tags.append((t,d));self.inld=t=='script' and d.get('type')=='application/ld+json' or self.inld
 def handle_endtag(self,t):
  if t=='script':self.inld=False
 def handle_data(self,d):
  if self.inld:self.ld.append(d)
urls=[e.text for e in ET.parse(root/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
for url in urls:
 rel=url.removeprefix(base+'/');file=root/(rel+'index.html' if not rel.endswith('.html') else rel);p=P();p.feed(file.read_text());tags=p.tags
 assert sum(t=='h1' for t,a in tags)==1,file
 assert any(t=='meta' and a.get('name')=='description' and len(a.get('content',''))>10 for t,a in tags),file
 assert any(t=='link' and a.get('rel')=='canonical' and a.get('href')==url for t,a in tags),file
 assert 'noindex' not in file.read_text(),file
 assert len(json.loads(''.join(p.ld)))>=2,file
 for t,a in tags:
  if t=='img':assert all(k in a for k in ['alt','width','height']),file
  ref=a.get('href') if t in ['a','link'] else a.get('src') if t in ['img','script'] else None
  if not ref or ref.startswith('#') or urlparse(ref).scheme:continue
  assert ref.startswith(prefix+'/'),(file,ref)
  target=root/ref.removeprefix(prefix+'/');target=target/'index.html' if ref.endswith('/') else target
  assert target.exists(),(file,target)
 print('PASS',rel or '/')
print('Validated',len(urls),'pages: metadata, schema, local links, image dimensions and sitemap')
