# object for writing sheets to one workbook
writer = pd.ExcelWriter('filled_sourcing_recs.xlsx') 

# write each sheet to the workbook
for sheet, df in dfs.items():
    df.to_excel(writer, sheet, index=False)

# save the workbook
writer.save()
