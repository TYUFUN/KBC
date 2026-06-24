import webview
class Api:
    def select_file(self):
        if not window:
            return "Window not created"
        res = window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=False, file_types=("Executable files (*.exe)", "All files (*.*)"))
        if res:
            return res
        return "No file selected"
    
api = Api()
window = webview.create_window('KBC', 'front/index.html', maximized=True,
    resizable=False,
    easy_drag=True,
    background_color="#000000", js_api=api) #html= для передачи переменной в вебвью
webview.start() #debug=True can help solve problems