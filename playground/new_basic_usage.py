from linovelib2epub.linovel import Linovelib2Epub

# warning!: must run within __main__ module guard due to process spawn issue.
if __name__ == '__main__':
    # linovelib_epub = Linovelib2Epub(book_id=3573, clean_artifacts=False, select_volume_mode=True)
    # linovelib_epub = Linovelib2Epub(book_id=3573, clean_artifacts=False)
    linovelib_epub = Linovelib2Epub(book_id=1068,divide_volume=True ,clean_artifacts=False)
    linovelib_epub.run()
