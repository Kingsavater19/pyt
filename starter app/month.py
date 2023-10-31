month_of_years={"Jan":"january", "Feb":"February","Mar":"March","May":"May","Jun":"June","Jul":"July",
                "Aug":"August","Sep":"September","Oct":"October","Nov":"November", "Dec":"December"}

retreive=str(input("Enter the month of the Year :"))


retreivemonth=str(month_of_years.get(retreive,"invald"))

print(retreivemonth)