
def css():
    init = [
        '*,;',
        '::before,;',
        '::after {;',
        '    box-sizing: border-box;',
        '    margin: 0;',
        '    padding: 0;',
        '};',
        '.bg {;',
        '    background: url(;',
        '        "https://images.unsplash.com/photo-1631515998058-69359a50da68?ixlib");',
        '    background-repeat: no-repeat;',
        '    background-attachment: fixed;',
        '    background-size: cover;',
        '    height: 100 %;',
        '    padding-top: 15 %;',
        '};'
    ]
    base = ["margin: auto;",
            "box-shadow: 0 0 10px 0 rgba(0, 0, 0, .4);",
            "border-radius: 5px;",
            "position: relative;",
            "z-index: 1;",
            "background: inherit;",
            "overflow: hidden;",
            "display: flex;",
            "justify-content: center;",
            "align-items: center;",
            "flex-direction: column;"]
    after = [

        'content: "";',
        'position: absolute;',
        'background: inherit;',
        'z-index: -1;',
        'inset: 0;',
        'filter: blur(10px);',
        'margin: -20px;'
    ]
    res = []
    for z in range(len(init)):
        res.append(init[z])
    for k in range(1, 11):
        for i in range(1, 11):
            res.append(f".container-{k}-{i} {{")
            for j in range(len(base)):
                res.append(base[j])
            res.append(f"height: {i*10}%;")
            res.append(f"width: {k*10}%;")
            res.append("}")
            res.append(f".container-{k}-{i}::before {{")
            for j in range(len(after)):
                res.append(after[j])
            res.append("}")
    return res


with open("glass/donnees.css", "w") as f:
    for i in css():
        f.write(i + "\n")
