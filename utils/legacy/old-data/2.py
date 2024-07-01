from typing import Union

from fastapi import FastAPI
from pydantic import BaseSettings


class EnvSettings(BaseSettings):
    pass

    
settings = EnvSettings()
app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "wip :/"}
 
@app.get("/api/offsets/11941010")
def read_offsets_11941010():
    offsets = '{"0":{"a":true,"o":[75862808,32,16,384,24]},"1":{"a":true,"o":[75862808,32,16,3528,16]},"2":{"a":true,"o":[75862808,32,3360,32,0,20]},"3":{"a":true,"o":[[76500312,0,24,0,984,0,24,8,1112],[76500312,0,24,0,984,0,24,8,1144]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}
 
@app.get("/api/offsets/11950020")
def read_offsets_11950020():
    offsets = '{"0":{"a":true,"o":[76448184,32,16,392,24]},"1":{"a":true,"o":[76448184,32,16,3504,16]},"2":{"a":true,"o":[76448184,32,3336,32,0,20]},"3":{"a":true,"o":[[77026976,0,24,0,976,0,24,8,1112],[77026976,0,24,0,976,0,24,8,1144]]}}' 

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}
 
@app.get("/api/offsets/11951010")
def read_offsets_11951010():
    offsets = '{"0":{"a":true,"o":[76443928,32,16,392,24]},"1":{"a":true,"o":[76443928,32,16,3504,16]},"2":{"a":true,"o":[76443928,32,3336,32,0,20]},"3":{"a":true,"o":[[77022352,0,24,0,976,0,24,8,1112],[77022352,0,24,0,976,0,24,8,1144]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/11960030")
def read_offsets_11960030():
    offsets = '{"0":{"a":true,"o":[77215864,32,16,392,24]},"1":{"a":true,"o":[77215864,32,16,3512,16]},"2":{"a":true,"o":[77218488,32,3328,32,0,20]},"3":{"a":true,"o":[[77795792,0,24,0,984,0,32,8,1072],[77795792,0,24,0,984,0,32,8,1104]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}


@app.get("/api/offsets/11962010")
def read_offsets_11962010():
    offsets = '{"0":{"a":true,"o":[77181752,32,16,392,24]},"1":{"a":true,"o":[77181752,32,16,3512,16]},"2":{"a":true,"o":[77181752,32,3328,32,0,20]},"3":{"a":true,"o":[[77758992,0,24,0,984,0,32,8,1072],[77758992,0,24,0,984,0,32,8,1104]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/11963010")
def read_offsets_11963010():
    offsets = '{"0":{"a":true,"o":[77211992,32,16,392,24]},"1":{"a":true,"o":[77211992,32,16,3512,16]},"2":{"a":true,"o":[77211992,32,3328,32,0,20]},"3":{"a":true,"o":[[77791872,0,24,0,984,0,32,8,1072],[77791872,0,24,0,984,0,32,8,1104]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/11970020")
def read_offsets_11970020():
    offsets = '{"0":{"a":true,"o":[78607432,32,16,400,24]},"1":{"a":true,"o":[78607432,32,16,3520,16]},"2":{"a":true,"o":[78607432,32,3336,32,0,20]},"3":{"a":true,"o":[[79187616,0,24,0,968,0,32,8,1096],[79187616,0,24,0,968,0,32,8,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/11971020")
def read_offsets_11971020():
    offsets = '{"0":{"a":true,"o":[78615608,32,16,400,24]},"1":{"a":true,"o":[78615608,32,16,3520,16]},"2":{"a":true,"o":[78615608,32,3336,32,0,20]},"3":{"a":true,"o":[[79193088,0,24,0,968,0,32,8,1096],[79193088,0,24,0,968,0,32,8,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/11973020")
def read_offsets_11973020():
    offsets = '{"0":{"a":true,"o":[78615608,32,16,400,24]},"1":{"a":true,"o":[78615608,32,16,3520,16]},"2":{"a":true,"o":[78615608,32,3336,32,0,20]},"3":{"a":true,"o":[[79193056,0,24,0,968,0,32,8,1096],[79193056,0,24,0,968,0,32,8,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/11980020")
def read_offsets_11980020():
    offsets = '{"0":{"a":true,"o":[81848808,32,16,400,24]},"1":{"a":true,"o":[81848808,32,16,3528,16]},"2":{"a":true,"o":[81851224,32,3344,32,0,20]},"3":{"a":true,"o":[[82434616,0,24,0,968,0,32,16,1096],[82434616,0,24,0,968,0,32,16,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/11981010")
def read_offsets_11981010():
    offsets = '{"0":{"a":true,"o":[81852872,32,16,400,24]},"1":{"a":true,"o":[81852872,32,16,3528,16]},"2":{"a":true,"o":[81852872,32,3344,32,0,20]},"3":{"a":true,"o":[[82439064,0,24,0,968,0,32,16,1096],[82439064,0,24,0,968,0,32,16,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/11983010")
def read_offsets_11983010():
    offsets = '{"0":{"a":true,"o":[81857320,32,16,400,24]},"1":{"a":true,"o":[81857320,32,16,3528,16]},"2":{"a":true,"o":[81857320,32,3344,32,0,20]},"3":{"a":true,"o":[[82443000,0,24,0,968,0,32,16,1096],[82443000,0,24,0,968,0,32,16,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12010")
def read_offsets_12010():
    offsets = '{"0":{"a":true,"o":[83921480,32,16,400,24]},"1":{"a":true,"o":[83921480,32,16,3536,16]},"2":{"a":true,"o":[83921480,32,3352,32,0,20]},"3":{"a":true,"o":[[84518272,0,24,0,968,0,24,88,1096],[84518272,0,24,0,968,0,24,88,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/1201020")
def read_offsets_1201020():
    offsets = '{"0":{"a":true,"o":[83921480,32,16,400,24]},"1":{"a":true,"o":[83921480,32,16,3536,16]},"2":{"a":true,"o":[83921480,32,3352,32,0,20]},"3":{"a":true,"o":[[84518224,0,24,0,968,0,24,88,1096],[84518224,0,24,0,968,0,24,88,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12010010")
def read_offsets_12010010():
    offsets = '{"0":{"a":true,"o":[86100488,32,16,400,24]},"1":{"a":true,"o":[86100488,32,16,3536,16]},"2":{"a":true,"o":[86100488,32,3352,32,0,20]},"3":{"a":true,"o":[[86685888,0,24,0,992,0,104,96,1096],[86685888,0,24,0,992,0,104,96,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12012010")
def read_offsets_12012010():
    offsets = '{"0":{"a":true,"o":[86100488,32,16,400,24]},"1":{"a":true,"o":[86100488,32,16,3536,16]},"2":{"a":true,"o":[86100488,32,3352,32,0,20]},"3":{"a":true,"o":[[86685792,0,24,0,992,0,104,96,1096],[86685792,0,24,0,992,0,104,96,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12015010")
def read_offsets_12015010():
    offsets = '{"0":{"a":true,"o":[86100488,32,16,400,24]},"1":{"a":true,"o":[86100488,32,16,3536,16]},"2":{"a":true,"o":[86100488,32,3352,32,0,20]},"3":{"a":true,"o":[[86685856,0,24,0,992,0,104,96,1096],[86685856,0,24,0,992,0,104,96,1128]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}


@app.get("/api/offsets/12030020")
def read_offsets_12030020():
    offsets = '{"0":{"a":true,"o":[89082312,32,16,408,24]},"1":{"a":true,"o":[89078888,32,16,3552,16]},"2":{"a":true,"o":[89078888,32,3368,32,0,20]},"3":{"a":true,"o":[[89673864,0,24,0,992,0,40,96,1080],[89673864,0,24,0,992,0,40,96,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12031010")
def read_offsets_12031010():
    offsets = '{"0":{"a":true,"o":[89082552,32,16,408,24]},"1":{"a":true,"o":[89082552,32,16,3552,16]},"2":{"a":true,"o":[89082552,32,3368,32,0,20]},"3":{"a":true,"o":[[89674120,0,24,0,992,0,40,96,1080],[89674120,0,24,0,992,0,40,96,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}


@app.get("/api/offsets/12032030")
def read_offsets_12032030():
    offsets = '{"0":{"a":true,"o":[89082440,32,16,408,24]},"1":{"a":true,"o":[89082440,32,16,3552,16]},"2":{"a":true,"o":[89082440,32,3368,32,0,20]},"3":{"a":true,"o":[[89674040,0,24,0,992,0,40,96,1080],[89674040,0,24,0,992,0,40,96,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}


@app.get("/api/offsets/12040010")
def read_offsets_12040010():
    offsets = '{"0":{"a":true,"o":[89989448,32,16,432,24]},"1":{"a":true,"o":[89989448,32,16,3576,16]},"2":{"a":true,"o":[89989448,32,3392,32,0,20]},"3":{"a":true,"o":[[90539456,0,32,8,16,840,56,224,1080],[90539456,0,32,8,16,840,56,224,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}


@app.get("/api/offsets/12041020")
def read_offsets_12041020():
    offsets = '{"0":{"a":true,"o":[89986360,32,16,432,24]},"1":{"a":true,"o":[89986360,32,16,3576,16]},"2":{"a":true,"o":[89986360,32,3392,32,0,20]},"3":{"a":true,"o":[[90539552,0,32,8,16,840,56,224,1080],[90539552,0,32,8,16,840,56,224,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12050030")
def read_offsets_12050030():
    offsets = '{"0":{"a":true,"o":[91423160,32,16,432,24]},"1":{"a":true,"o":[91423160,32,16,3584,16]},"2":{"a":true,"o":[91423160,32,3400,32,0,20]},"3":{"a":true,"o":[[91897040,0,32,8,16,840,56,224,1080],[91897040,0,32,8,16,840,56,224,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12051010")
def read_offsets_12051010():
    offsets = '{"0":{"a":true,"o":[91419976,32,16,432,24]},"1":{"a":true,"o":[91419976,32,16,3584,16]},"2":{"a":true,"o":[91419976,32,3400,32,0,20]},"3":{"a":true,"o":[[91893648,0,32,8,16,840,56,224,1080],[91893648,0,32,8,16,840,56,224,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12060040")
def read_offsets_12060040():
    offsets = '{"0":{"a":true,"o":[91960040,32,16,432,24]},"1":{"a":true,"o":[91960040,32,16,3592,16]},"2":{"a":true,"o":[91956248,32,3408,32,0,20]},"3":{"a":true,"o":[[92423960,0,32,8,16,712,56,224,1080],[92423960,0,32,8,16,712,56,224,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12062010")
def read_offsets_12062010():
    offsets = '{"0":{"a":true,"o":[91964120,32,16,432,24]},"1":{"a":true,"o":[91964120,32,16,3592,16]},"2":{"a":true,"o":[91964120,32,3408,32,0,20]},"3":{"a":true,"o":[[92428136,0,32,8,16,712,56,224,1080],[92428136,0,32,8,16,712,56,224,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

# got deprecated by Mojang
@app.get("/api/offsets/12071010")
def read_offsets_12071010():
    offsets = '{"0":{"a":true,"o":[92656760,32,16,432,24]},"1":{"a":true,"o":[92656760,32,16,3592,16]},"2":{"a":true,"o":[92656760,32,3408,32,0,20]},"3":{"a":true,"o":[[93190600,0,32,8,16,712,56,224,1080],[93190600,0,32,8,16,712,56,224,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12072010")
def read_offsets_12072010():
    offsets = '{"0":{"a":true,"o":[92656792,32,16,432,24]},"1":{"a":true,"o":[92656792,32,16,3592,16]},"2":{"a":true,"o":[92656792,32,3408,32,0,20]},"3":{"a":true,"o":[[93190648,0,32,8,16,712,56,224,1080],[93190648,0,32,8,16,712,56,224,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12073010")
def read_offsets_12073010():
    offsets = '{"0":{"a":true,"o":[92671560,32,16,432,24]},"1":{"a":true,"o":[92671560,32,16,3592,16]},"2":{"a":true,"o":[92671560,32,3408,32,0,20]},"3":{"a":true,"o":[[93212216,0,32,8,16,712,56,224,1080],[93212216,0,32,8,16,712,56,224,1112]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12080050")
def read_offsets_12080050():
    offsets = '{"0":{"a":true,"o":[95457144,32,16,432,24]},"1":{"a":true,"o":[95457144,32,16,3584,16]},"2":{"a":true,"o":[95457144,32,3400,32,0,20]},"3":{"a":true,"o":[[96021816,0,32,8,16,712,56,224,1112],[96021816,0,32,8,16,712,56,224,1144]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12081010")
def read_offsets_12081010():
    offsets = '{"0":{"a":true,"o":[95457144,32,16,432,24]},"1":{"a":true,"o":[95457144,32,16,3584,16]},"2":{"a":true,"o":[95457144,32,3400,32,0,20]},"3":{"a":true,"o":[[96021816,0,32,8,16,712,56,224,1112],[96021816,0,32,8,16,712,56,224,1144]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/12130")
def read_offsets_12130():
    offsets = '{"0":{"a":true,"o":[94366264,32,16,432,24]},"1":{"a":true,"o":[94366264,32,16,3584,16]},"2":{"a":true,"o":[94366264,32,3400,32,0,20]},"3":{"a":true,"o":[[94690032,0,32,8,16,712,56,224,1112],[94690032,0,32,8,16,712,56,224,1144]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}

@app.get("/api/offsets/1211030")
def read_offsets_1211030():
    offsets = '{"0":{"a":true,"o":[94378744,32,16,432,24]},"1":{"a":true,"o":[94378744,32,16,3584,16]},"2":{"a":true,"o":[94378744,32,3400,32,0,20]},"3":{"a":true,"o":[[94702480,0,32,8,16,712,56,224,1112],[94702480,0,32,8,16,712,56,224,1144]]}}'

    return {"message": "Successfully found offsets!", "offsets": offsets, "status": 200}
