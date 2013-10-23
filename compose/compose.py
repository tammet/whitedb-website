#!/usr/bin/python


# ASCIIDOC_XSL=/usr/share/asciidoc/docbook-xsl/ ./gendoc.sh Doc

import sys,string

inpath="../templates/"
outpath="../htdocs/"

template="page.html"
rawprefix="raw_"
templatesuffix="_template"
raw=["c_api","python_api","tutorial","install","tools"]
rawtrans={"install":"Install.html","tutorial":"Tutorial.html",
  "python_api":"python.html","c_api":"Manual.html","tools":"Utilities.html"}
pages=["index","tutorial","speed","scenarios","api","c_api","python_api","tools","download","install","licence","contact"]
nocontents=["install"]

urlchanges={
  "href=\"python.html\"":"href=\"python_api.html\"", 
  "href=\"Manual.html\"":"href=\"c_api.html\"",
  "href=\"Tutorial.html\"":"href=\"tutorial.html\"",
  #"<em>Examples/tut1.c</em>":"<a href=\"code/tut1.c\">Examples/tut1.c</a>",
  #"<em>Examples/tut2.c</em>":"<a href=\"code/tut2.c\">Examples/tut2.c</a>",  
  "<em>Examples/demo.c</em>":"<a href=\"code/demo.c\">Examples/demo.c</a>",
  "<em>Examples/query.c</em>":"<a href=\"code/query.c\">Examples/query.c</a>",
  "<em>Examples/mem1.c</em>":"<a href=\"code/mem1.c\">Examples/mem1.c</a>",
  "<em>Examples/dserve.c</em>":"<a href=\"code/dserve.c\">Examples/dserve.c</a>",
  "<em>dserve.c</em>":"<a href=\"code/dserve.c\">dserve.c</a>",
  "<em>Examples/raptortry.c</em>":"<a href=\"code/raptortry.c\">Examples/raptortry.c</a>",
  "<em>Examples/compile_demo.sh</em>":"<a href=\"code/compile_demo.sh\">Examples/compile_demo.sh</a>",
  "<em>Examples/compile_query.sh</em>":"<a href=\"code/compile_query.sh\">Examples/compile_query.sh</a>",
  "<img src=\"images/icons/note.png\" alt=\"[Note]\">": "",
  "<img alt=\"[Note]\" src=\"images/icons/note.png\" />": "<span class=\"label label-info\">!</span>"
}
        

def main():
  # create temporary files for raw auto-generated docs
  for page in raw:
    fname=inpath+rawtrans[page]   
    #fname=inpath+rawprefix+page+".html"
    print fname
    try:
      f=open(fname,"r")
      rs=f.read()
      f.close()
    except:
      continue    
    rs=mod_raw_html(rs)      
    toc_marker="<dl class=\"toc\">"
    content_marker="</div>"
    end_marker="</body></html>"    
    toc_loc=rs.find(toc_marker)
    content_loc=rs.find(content_marker,toc_loc)
    end_loc=rs.find(end_marker,content_loc)
    toc=rs[toc_loc:content_loc]
    #print toc_loc,toc
    if page in nocontents:
      content=""
    else:  
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

def mod_raw_html(raw):
  nxt=raw
  for k in urlchanges:
    nxt=nxt.replace(k,urlchanges[k])
  return nxt      
  
main()