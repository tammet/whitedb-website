#!/usr/bin/python

import sys,string

inpath="../templates/"
outpath="../htdocs/"

template="page.html"
rawprefix="raw_"
templatesuffix="_template"
raw=["c_api","python_api","tutorial"]
pages=["index","tutorial","speed","scenarios","api","c_api","python_api","download","install","licence","contact"]

def main():
  # create temporary files for raw auto-generated docs
  for page in raw:
    fname=inpath+rawprefix+page+".html"
    print fname
    try:
      f=open(fname,"r")
      rs=f.read()
      f.close()
    except:
      continue      
    toc_marker="<dl class=\"toc\">"
    content_marker="</div>"
    end_marker="</body></html>"    
    toc_loc=rs.find(toc_marker)
    content_loc=rs.find(content_marker,toc_loc)
    end_loc=rs.find(end_marker,content_loc)
    toc=rs[toc_loc:content_loc]
    #print toc_loc,toc
    content="<div class=\"toc\">\n"+rs[toc_loc:content_loc]+"\n</div> <!-- inner toc end -->\n"
    content+=rs[content_loc+len(content_marker):end_loc]
    #print content_loc,end_loc,content
    classes={"toc":toc,"content":content}
    fname=inpath+page+templatesuffix+".html"
    print fname
    f=open(fname,"r")
    rs=f.read()
    f.close()
    tmpl=string.Template(rs) 
    out=tmpl.safe_substitute(classes)
    fname=inpath+page+".html"
    print fname
    f=open(fname,"w")
    f.write(out)
    f.close()
  #return
  
  # create final html pages
  fname=inpath+template
  f=open(fname,"r")
  rs=f.read()
  tmpl=string.Template(rs) 
  f.close()
  for p in pages:
    if p in raw:
      fname=inpath+p+".html"
    else:  
      fname=inpath+p+".html"
    try:
      f=open(fname,"r")
      content=f.read()
      #print content
      f.close()
    except:
      continue      
    classes={}
    for c in pages:
      classes[c]="dummy"
    classes[p]="active"
    classes["content"]=content    
    out=tmpl.safe_substitute(classes)
    fname=outpath+p+".html"
    f=open(fname,"w")
    f.write(out)
    f.close()
  
main()