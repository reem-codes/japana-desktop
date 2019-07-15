from japana.word_count import word_count
import os


def process(input, output, kana, asc, dictionary, progressbar):
    try:
        directory = os.path.dirname(output)

        original_umask = os.umask(0)
        try:
            if not os.path.exists(directory):
                os.makedirs(directory, 0o777)
        finally:
            os.umask(original_umask)

        with open(input, 'r') as f:
            text = f.read()

        words = word_count(text, kana, asc, dictionary, progress=progressbar)

        with open(output, "a") as o:
            o.truncate(0)
            for word in words:
                line = word['word'] + "\t"
                line += (word['meaning'] if word.get("meaning") else "-") + "\t"
                line += (word['pronunciation'] if word.get("pronunciation") else "-") + "\t"
                line += str(word['frequency']) + "\n"
                o.write(line)
        return True
    except:
        return False
