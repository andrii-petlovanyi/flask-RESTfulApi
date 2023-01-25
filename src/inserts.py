from datetime import date

from src import db
from src.models import Film


def populate_films():
    star_wars_1 = Film(
        title='Episode I – The Phantom Menace',
        release_date=date(1999, 5, 19),
        description='Star Wars: Episode I – The Phantom Menace is a 1999 American epic space opera film written and directed by George Lucas. It stars Liam Neeson, Ewan McGregor, Natalie Portman, Jake Lloyd, Ian McDiarmid, Anthony Daniels, Kenny Baker, Pernilla August, and Frank Oz. It is the fourth film in the Star Wars film series, the first film of the prequel trilogy and the first chronological chapter of the "Skywalker Saga". Set 32 years before the original trilogy, during the era of the Galactic Republic, the plot follows Jedi Master Qui-Gon Jinn and his apprentice Obi-Wan Kenobi as they try to protect Queen Padmé Amidala of Naboo in hopes of securing a peaceful end to an interplanetary trade dispute. Joined by Anakin Skywalker—a young slave with unusually strong natural powers of the Force—they simultaneously contend with the mysterious return of the Sith. The film was produced by Lucasfilm, with 20th Century Fox distributing.',
        distributed_by='Lucasfilm',
        length=133,
        rating=6.5,
    )
    star_wars_2 = Film(
        title='Episode II – Attack of the Clones',
        release_date=date(2002, 5, 16),
        description='Star Wars: Episode II – Attack of the Clones is a 2002 American epic space opera film directed by George Lucas and written by Lucas and Jonathan Hales. The sequel to The Phantom Menace (1999), it is the fifth film in the Star Wars film series and second chronological chapter of the "Skywalker Saga". The film stars Ewan McGregor, Natalie Portman, Hayden Christensen, Ian McDiarmid, Samuel L. Jackson, Christopher Lee, Anthony Daniels, Kenny Baker, and Frank Oz.',
        distributed_by='Lucasfilm',
        length=142,
        rating=6.6,
    )
    star_wars_3 = Film(
        title='Episode III – Revenge of the Sith',
        release_date=date(2005, 5, 19),
        description='Star Wars: Episode III – Revenge of the Sith is a 2005 American epic space opera film written and directed by George Lucas. It stars Ewan McGregor, Natalie Portman, Hayden Christensen, Ian McDiarmid, Samuel L. Jackson, Christopher Lee, Anthony Daniels, Kenny Baker and Frank Oz. The sequel to The Phantom Menace (1999) and Attack of the Clones (2002), it is the sixth film in the Star Wars film series, the final installment in the Star Wars prequel trilogy, and third chronological chapter of the "Skywalker Saga".',
        distributed_by='Lucasfilm',
        length=140,
        rating=7.6,
    )
    star_wars_4 = Film(
        title='Episode IV – A New Hope',
        release_date=date(1977, 5, 25),
        description='Star Wars (retroactively titled Star Wars: Episode IV – A New Hope) is a 1977 American epic space opera film written and directed by George Lucas, produced by Lucasfilm and distributed by 20th Century Fox. It is the first film in the Star Wars film series and fourth chronological chapter of the "Skywalker Saga". Set "a long time ago" in a fictional universe where the galaxy is ruled by the tyrannical Galactic Empire, the story focuses on a group of freedom fighters known as the Rebel Alliance, who aim to destroy the Empire\'s newest weapon, the Death Star. Luke Skywalker becomes caught in the conflict while learning the ways of a metaphysical power known as "the Force" from Jedi Master Obi-Wan Kenobi. The cast includes Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing, Alec Guinness, David Prowse, James Earl Jones, Anthony Daniels, Kenny Baker, and Peter Mayhew.',
        distributed_by='Lucas Film',
        length=121,
        rating=8.6,
    )
    star_wars_5 = Film(
        title='Episode V – The Empire Strikes Back',
        release_date=date(1980, 5, 21),
        description='The Empire Strikes Back (also known as Star Wars: Episode V – The Empire Strikes Back) is a 1980 American epic space opera film directed by Irvin Kershner from a screenplay by Leigh Brackett and Lawrence Kasdan, based on a story by George Lucas. The sequel to Star Wars (1977),[b] it is the second film in the Star Wars film series and the fifth chronological chapter of the "Skywalker Saga". Set three years after the events of Star Wars, the film recounts the battle between the malevolent Galactic Empire, led by the Emperor, and the Rebel Alliance, led by Princess Leia. Luke Skywalker trains to master the Force so he can confront the powerful Sith lord, Darth Vader. The ensemble cast includes Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew, and Frank Oz.',
        distributed_by='Lucas Film',
        length=124,
        rating=8.7,
    )
    star_wars_6 = Film(
        title='Episode VI – Return of the Jedi',
        release_date=date(1983, 5, 25),
        description='Return of the Jedi (also known as Star Wars: Episode VI – Return of the Jedi) is a 1983 American epic space opera film directed by Richard Marquand. The screenplay is by Lawrence Kasdan and George Lucas from a story by Lucas, who was also the executive producer. The sequel to Star Wars (1977)[a] and The Empire Strikes Back (1980), it is the third installment in the original Star Wars trilogy, the third film to be produced, and the sixth chronological film in the "Skywalker Saga". The film stars Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew and Frank Oz.',
        distributed_by='Lucas Film',
        length=132,
        rating=8.3,
    )
    star_wars_7 = Film(
        title='Episode VII – The Force Awakens',
        release_date=date(2015, 12, 18),
        description='Star Wars: The Force Awakens (also known as Star Wars: Episode VII – The Force Awakens) is a 2015 American epic space opera film produced, co-written, and directed by J. J. Abrams. The sequel to Return of the Jedi (1983), it is the seventh film in the "Skywalker Saga". Set thirty years after Return of the Jedi, The Force Awakens follows Rey, Finn, Poe Dameron, and Han Solo\'s search for Luke Skywalker and their fight in the Resistance, led by General Leia Organa and veterans of the Rebel Alliance, against Kylo Ren and the First Order, a successor to the Galactic Empire. The ensemble cast includes Harrison Ford, Mark Hamill, Carrie Fisher, Adam Driver, Daisy Ridley, John Boyega, Oscar Isaac, Lupita Nyong\'o, Andy Serkis, Domhnall Gleeson, Anthony Daniels, Peter Mayhew, and Max von Sydow.',
        distributed_by='Lucas Film',
        length=138,
        rating=7.8,
    )
    star_wars_8 = Film(
        title='Episode VIII – The Last Jedi',
        release_date=date(2017, 12, 15),
        description='Star Wars: The Last Jedi (also known as Star Wars: Episode VIII – The Last Jedi) is a 2017 American epic space opera film written and directed by Rian Johnson. Produced by Lucasfilm and distributed by Walt Disney Studios Motion Pictures, it is the second installment of the Star Wars sequel trilogy, following The Force Awakens (2015), and the eighth episode of the nine-part "Skywalker saga". The film\'s ensemble cast includes Mark Hamill, Carrie Fisher, Adam Driver, Daisy Ridley, John Boyega, Oscar Isaac, Andy Serkis, Lupita Nyong\'o, Domhnall Gleeson, Anthony Daniels, Gwendoline Christie, Kelly Marie Tran, Laura Dern, and Benicio del Toro. The Last Jedi follows Rey as she seeks the aid of Luke Skywalker, in hopes of turning the tide for the Resistance in the fight against Kylo Ren and the First Order, while General Leia Organa, Finn, and Poe Dameron attempt to escape a First Order attack on the dwindling Resistance fleet. The film features the first posthumous film performance by Fisher, who died in December 2016, and the film is dedicated to her memory.[5]',
        distributed_by='Lucas Film',
        length=158,
        rating=6.9,
    )
    star_wars_9 = Film(
        title='Episode IX – The Rise of Skywalker',
        release_date=date(2019, 12, 20),
        description='Star Wars: The Rise of Skywalker (also known as Star Wars: Episode IX – The Rise of Skywalker) is a 2019 American epic space opera film produced, co-written, and directed by J. J. Abrams. Produced by Lucasfilm and Abrams\' production company Bad Robot Productions, and distributed by Walt Disney Studios Motion Pictures, it is the third installment of the Star Wars sequel trilogy, following The Force Awakens (2015) and The Last Jedi (2017), and the final episode of the nine-part "Skywalker saga".[a] Its ensemble cast includes Carrie Fisher,[b] Mark Hamill, Adam Driver, Daisy Ridley, John Boyega, Oscar Isaac, Anthony Daniels, Naomi Ackie, Domhnall Gleeson, Richard E. Grant, Lupita Nyong\'o, Keri Russell, Joonas Suotamo, Kelly Marie Tran, Ian McDiarmid, and Billy Dee Williams. The Rise of Skywalker follows Rey, Finn, and Poe Dameron as they lead the Resistance\'s final stand against Supreme Leader Kylo Ren and the First Order, who are aided by the return of the Galactic Emperor, Palpatine.',
        distributed_by='Lucas Film',
        length=142,
        rating=6.5,
    )

    db.session.add(star_wars_1)
    db.session.add(star_wars_2)
    db.session.add(star_wars_3)
    db.session.add(star_wars_4)
    db.session.add(star_wars_5)
    db.session.add(star_wars_6)
    db.session.add(star_wars_7)
    db.session.add(star_wars_8)
    db.session.add(star_wars_9)


    db.session.commit()
    db.create_all()
    db.session.close()


if __name__ == '__main__':
    print('Populate db...')
    populate_films()
    print('Successfully populate!')
