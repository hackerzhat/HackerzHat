```
██   ██ ███████ ███████ 
 ██ ██  ██      ██      
  ███   ███████ ███████ 
 ██ ██       ██      ██ 
██   ██ ███████ ███████ 
```                
HackerzHatz XSS tools for fuzzing and exploitation.

## Inject a JavaScript file into a PDF file
Tool used: [JS2PDFInjector](https://github.com/cornerpirate/JS2PDFInjector)

Contents of the file [test01.js](CrossSiteScripting/Upload_pdf_for_xss/test01.js):
```javascript
app.alert("XSS")
```

Pdf with injected js:
- [Payload with alert XSS](CrossSiteScripting/Upload_pdf_for_xss/Payload01.pdf)
