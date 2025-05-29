const CHARACTER_IMAGES = {
    // Tu diccionario de personajes aquí
    0: "mario.png",
    1: "fox.png",
    2: "donkey_kong.png",
    3: "samus.png",
    4: "luigi.png",
    5: "link.png",
    6: "yoshi.png",
    7: "captain_falcon.png",
    8: "kirby.png",
    9: "pikachu.png",
    10: "jigglypuff.png",
    11: "ness.png",
    
    //# Nuevos personajes (desde 0x1D)
    29: "falco.png",
    30: "ganondorf.png",       // GND
    31: "young_link.png",      // YLINK
    32: "dr_mario.png",        // DRM
    33: "wario.png",
    34: "dark_samus.png",      // DSAMUS
    35: "link.png",            // ELINK (usamos link.png)
    36: "samus.png",           // J Samus
    37: "ness.png",            // J Ness
    38: "lucas.png",
    39: "link.png",            // J Link
    40: "captain_falcon.png",  // J Falcon
    41: "fox.png",             // J Fox
    42: "mario.png",           // J Mario
    43: "luigi.png",           // J Luigi
    44: "donkey_kong.png",     // J DK
    45: "pikachu.png",         // E Pikachu
    46: "jigglypuff.png",      // J Jigglypuff
    47: "jigglypuff.png",      // E Jigglypuff
    48: "kirby.png",           // J Kirby
    49: "yoshi.png",           // J Yoshi
    50: "pikachu.png",         // J Pikachu
    51: "samus.png",           // E Samus
    52: "bowser.png",
    53: "giga_bowser.png",     // GBOWSER
    54: "mad_piano.png",       // Piano
    55: "wolf.png",
    56: "conker.png",
    57: "mewtwo.png",          // MTWO
    58: "marth.png",
    59: "sonic.png",
    60: "random.png",          // Sandbag (no hay imagen específica)
    61: "super_sonic.png",     // SSONIC
    62: "sheik.png",
    63: "marina.png",
    64: "dedede.png",          // DEDEDE
    65: "goemon.png",
    66: "peppy.png",
    67: "slippy.png",
    68: "banjo.png",           // BANJO
    69: "metal_luigi.png",     // MLUIGI
    70: "ebisumaru.png",
    71: "dragon_king.png",     // DRAGONKING
    
    // Especial
    222: "random.png"          // Random
};

function updateData() {
    fetch('game_data.json')
        .then(response => response.json())
        .then(data => {
            // Actualizar jugadores
            updatePlayer(data.p1, 'p1');
            updatePlayer(data.p2, 'p2');
            
            // Actualizar información del partido
            document.getElementById('stage').textContent = `Stage: ${data.stage}`;
            document.getElementById('playing').textContent = `Playing: ${data.playing}`;
            document.getElementById('state').textContent = data.state;
            document.getElementById('total').textContent = `Total: ${data.total}`;
        });
}

function updatePlayer(playerData, prefix) {
    // Actualizar datos básicos
    document.getElementById(`${prefix}-name`).textContent = playerData.name;
    document.getElementById(`${prefix}-wins`).textContent = playerData.wins;
    document.getElementById(`${prefix}-percent`).textContent = `${playerData.win_percent}%`;
    
    // Actualizar imagen del personaje (con cache busting)
    const characterImg = document.getElementById(`${prefix}-character`);
    characterImg.src = `assets/characters/${playerData.character}`;
    
    // Actualizar barra de daño
    const damageFill = document.getElementById(`${prefix}-damage`);
    const currentDamage = parseFloat(playerData.damage); // Eliminar toFixed()
    const maxDamage = 130; // Máximo a 130%
    const width = Math.min((currentDamage / maxDamage) * 100, 100);
    
    // Sistema de color mejorado
    let color;
    if (currentDamage < 50) {
        color = '#00ff00'; // Verde
    } else if (currentDamage < 100) {
        color = '#ffd700'; // Amarillo
    } else {
        color = '#ff0000'; // Rojo
    }

    damageFill.style.width = `${width}%`;
    damageFill.style.background = `
        linear-gradient(
            to right,
            ${color} 0%,
            ${color} 80%,
            rgba(255, 255, 255, 0.3) 100%
        )`;
}



// Actualizar cada 500ms
setInterval(updateData, 150);