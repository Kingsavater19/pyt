month_of_years={"Jan":"january", "Feb":"February","Mar":"March","May":"May","Jun":"June","Jul":"July",
                "Aug":"August","Sep":"September","Oct":"October","Nov":"November", "Dec":"December"}
print(month_of_years["Aug"])
print(month_of_years.get("Dec"))
print(month_of_years.get("luv","not a vaild key"))