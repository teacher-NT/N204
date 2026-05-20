
import wikipedia as wk

wk.set_lang("uz")
page = wk.page("Tashkent")

print(page.summary)