Private Sub 分拆工作表()

Dim sht As Worksheet

Dim MyBook As Workbook

Set MyBook = ActiveWorkbook

For Each sht In MyBook.Sheets

sht.Copy

ActiveWorkbook.SaveAs Filename:=MyBook.Path & "\" & sht.Name, FileFormat:=xlOpenXMLWorkbook '将工作簿另存为EXCEL默认格式

ActiveWorkbook.Close

Next

MsgBox "文件分拆完毕!"

End Sub