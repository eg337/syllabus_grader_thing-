import gspread

gc = gspread.oauth()

# Open a sheet from a spreadsheet in one go
wks = gc.create("Where is the money Lebowski?")

# Update a range of cells using the top left corner address
wks.update([[1, 2], [3, 4]], "A1")

# Or update a single cell
wks.update_acell("B42", "it's down there somewhere, let me take another look.")

# Format the header
wks.format('A1:B1', {'textFormat': {'bold': True}})