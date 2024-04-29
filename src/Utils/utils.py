import os


class Utils:
    @classmethod
    def text_appender(cls, root, text):
        path = os.path.join(root, text)
        # Check if .gitignore file exists
        if not os.path.exists(path):
            cls.file_writer_add_text(path, text, "w")
        else:
            # Append directory pattern to .gitignore file
            cls.file_writer_add_text(path, text, "a")

    @classmethod
    def file_writer_add_text(cls, file, text, method):
        if method not in ["w", "a"]:
            return False
        mode = "w" if method == "w" else "a"
        try:
            with open(file, mode) as f:
                if text + "\n" in f.read_lines():
                    return True
                f.write(f"{text}\n")
            return True
        except IOError:
            return False
