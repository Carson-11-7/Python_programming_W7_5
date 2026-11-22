DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",)

class TIMESTAMP:
    weekday = ""
    hour = 0
    consumption = 0.0
    price = 0.0

class DAY_USAGE:
    weekday = ""
    usage = 0.0
    cost = 0.0

def readFile(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')
    PTimestamps.clear()
    filehandle = open(PFilename, "r", encoding="utf-8")
    firstLine = True

    for line in filehandle:
        if firstLine:          # skip header row
            firstLine = False
            continue
        if line == "\n":       # skip empty lines
            continue
        row = line.rstrip()
        columns = row.split(DELIMITER)
        timestamp = TIMESTAMP()
        timestamp.weekday = columns[0]
        timestamp.hour = int(columns[1])
        timestamp.consumption = float(columns[2])
        timestamp.price = float(columns[3])
        PTimestamps.append(timestamp)
        columns.clear()
    filehandle.close()
    return None

def analyseTimestamps(PTimestamps: list[TIMESTAMP], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    days: list[DAY_USAGE] = []


    for name in WEEKDAYS:
        day = DAY_USAGE()
        day.weekday = name
        days.append(day)  


    for timestamp in PTimestamps:
        for day in days:
            if timestamp.weekday == day.weekday:
                day.usage += timestamp.consumption
                day.cost += timestamp.consumption * timestamp.price
    PResults.append("### Electricity consumption summary ###")
    
    for day in days:
        PResults.append(
            f" - {day.weekday} usage {day.usage:.2f} kWh, "
            f"cost {day.cost:.2f} €"
            )
    PResults.append("### Electricity consumption summary ###")
    days.clear()
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for line in PResults:
        print(line)
    return None

def main() -> None:
    print("Program starting.")
    timestamps: list[TIMESTAMP] = []
    results: list[str] = []
    filename = input("Insert filename: ")
    readFile(filename, timestamps)
    analyseTimestamps(timestamps, results)
    displayResults(results)
    timestamps.clear()
    results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
