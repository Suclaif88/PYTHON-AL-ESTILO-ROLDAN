# Lista de nombres de películas
nombres_peliculas = [
    "The 355",
    "See for Me",
    "The Kindred",
    "American Siege",
    "Jethica",
    "Scream",
    "Belle",
    "Italian Studies",
    "Who We Are: A Chronicle of Racism in America",
    "Alter Ego",
    "The Pink Cloud",
    "The Conversation",
    "The Curse of La Patasola",
    "A Cops and Robbers Story",
    "Stoker Hills",
    "The Surprise Visit",
    "The King's Daughter",
    "Redeeming Love",
    "The Tiger Rising",
    "Unsilenced",
    "Simple Passion",
    "A Shot Through the Wall",
    "The Hunting",
    "Compartment Number 6",
    "Shortbus",
    "Gamestop: Rise of the Players",
    "Clean",
    "A Taste of Hunger",
    "Sundown",
    "Brighton 4th",
    "Charli XCX: Alone Together",
    "In the Forest",
    "They/Them/Us",
    "The Beatles: Get Back - The Rooftop Concert",
    "Music, Money, Madness... Jimi Hendrix in Maui",
    "Poly Styrene: I Am a Cliché",
    "Belle",
    "Jackass Forever",
    "Moonfall",
    "The Wolf and the Lion",
    "Only Fools Rush In",
    "The Worst Person in the World",
    "Breaking Bread",
    "Lingui",
    "The Long Night",
    "Last Survivors"
]

# Generar tarjetas para cada película
for i, titulo in enumerate(nombres_peliculas, start=2):
    # Generar el código HTML de la tarjeta
    codigo_html = f'''
    <div class="card">
        <img src="C-IMG/{i}.jpg" alt="Imagen">
        <div class="overlay">
            <h2>{titulo}</h2>
            <h3>Subtítulo</h3>
            <p>Descripción</p>
        </div>
    </div>
    '''
    
    # Imprimir el código HTML de la tarjeta
    print(codigo_html)
