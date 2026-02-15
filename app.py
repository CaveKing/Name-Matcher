from flask import Flask, render_template, request

app = Flask(__name__)

def generate_pairs(data):
    pairs = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                id1, name1 = data[i]
                id2, name2 = data[j]
                pairs.append({
                    "id_pair": f"{id1}/{id2}",
                    "name_pair": f"{name1}/{name2}"
                })
    return pairs

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        raw_data = request.form["names"]
        lines = raw_data.strip().split("\n")
        data = []
        for line in lines:
            parts = line.split(",")
            if len(parts) == 2:
                data.append((parts[0].strip(), parts[1].strip()))
        results = generate_pairs(data)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
