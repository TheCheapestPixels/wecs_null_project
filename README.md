wecs_null_project
=================

You want to develop a game, using Python, Panda3D, and WECS? (If you don't know one or more of those, there's a section on them after this one.) 

You don't want to write all the stuff that every game has to have? You want to get working on what makes your game *your* game? _Now_? Well, then _do_!

CAVEAT: Right now, you can only do prototypes, meaning that on startup, you set up your WECS `System`s and `Entity`s, and let it run. See "Coming soon", specifically "stage flow", below for details.


* Fork this project and rename it.
* CAVEAT: You can now *not* just run (I'm currently working on this bit!)...
  * `python setup.py build_apps` to build your project,
  * `python setup.py bdist_apps` to build it and create distributable packages.
  That's the bit I'm currently struggling through. At the beginning, the project has...
  * debug keybindings:
    * `escape` to exit the game (via `sys.exit()`)
    * `f9`: open / close the interactive console
    * `f10`: toggle the frame rate meter
    * `f11`: drop into a pdb session
    * `f12`: connect to the `pstats` server
  * three `System`s:
        wecs.cefconsole.UpdateWecsSubconsole
        wecs.cefconsole.WatchEntitiesInSubconsole
        wecs.panda3d.debug.DebugTools
  * no entities
* In `project_name/game/__init__.py`, add your `System`s to `system_types`, create your entities, and optionally run any other code you'd like to.

That's it. Plug in all the things that you have and need, then write the ones that you don't have, but need. Develop, test, build, distribute.


But I don't know...
-------------------

### Python

It's a popular and easy to learn programming language, and, dare I say it, aesthetically pleasing. You can install it via your platform's package manager, or from https://www.python.org/ where you also find the official documentation, including a tutorial. If that's not your preferred way of learning, there's hundreds of courses, tutorials, every kind of resource imaginable.


### Panda3D

Panda3D is a 3D engine that is used most often for games, but has also been used for engineering and visualization applications, art installations, amusement park rides, ...

Originally developed by Disney, it has been open sourced, and is now developed by its community. Despite rumors to the contrary, it is very much alive and close to the state of the art of technology.

Panda3D can be used with Python or C++. If C++ is your thing, I'm afraid that this boilerplate project is not for you, it's aimed at Python developers.

Unlike popular 3D engines, Panda3D does *not* come with an interactive game creation and editing toolchain. It is a library that offers you lots and lots of tools and building blocks, but you have to string them together with code. The reasoning is that any editor would make assumptions about how a game should be structured, limiting the design space of its user. Since flexibility is very high on the priority list of Panda3D development, designing an editor is a task that so far has not been tackled with confidence.

Model assets for Panda3D are usually created with Blender, though converters for other formats do exist, and Panda3D also reads glTF, which may become the de facto standard in the near future. Sound assets can be used as long as FFMPEG can read them.

You can find further information at https://www.panda3d.org/


### WECS

WECS is a set of strong assumptions about how a game should be structured, usually called ECS, "Entity, Component, System", or "Component System". Specifically, it assumes (and implements) these ideas:

* A game object, called an `Entity`, consists of a set of `Components`, and nothing more.
* Each `Component` describes the state of the `Entity` with regard to some aspect of its existence. A `Component` only stores data. It does not implement any functionality to manipulate that data.
* For each tick / frame of the game, there is a list of `System`s that are run in order. Consider them as a kind of Panda3D `Task`.
  * Each `System` has a set (actually a dictionary in code) of `entity_filters` that specify what `Component`s an `Entity` has to have to be processed.
  * When a `System` is being run, it receives a list of `Entity`s for each `entity_filter`, which contain all `Entity`s that match a given `entity_filter`.

This is an approach to game architecture that allows both a high degree of flexibility, and keeps each `System` manageably simple and isolated from other `System`s. That means less effort to maintain code, and that it is easy to combine separately developed game mechanics in the the same game. That also means that WECS can contain a lot of pre-made `System`s and `Component`s that you can just plug into your game.

You can find further information at https://github.com/TheCheapestPixels/wecs


Coming soon(-ish)
-----------------

As you saw in the introductory section, things are... not quite ready for prime time. There's one problem with this project itself right now:
* Deployment: I'm pushing that one forward one bug at a time...

There's at least three major things that'll have to be added to WECS. As soon as they are available there, you can just `pip upgrade WECS` to install them locally; `python setup.py bdist_apps` will automatically use the latest version. I am only making notice of them here as well because they are kind of meta, not being elegantly solvable by adding `System`s and `Component`s.
* Stage flow: Opening credits, main menu, new single player game, open in-game menu... I call each of these steps a `stage`. There needs to be a mechanism to tear down a WECS world's contents, and set up the next.
* Loading / saving games: There's no automatism yet to serialize the state of all `Component`s in the world that should be saved). Once that (and the corresponding deserialization) is added, saving and loading a game state should be a breeze.
* Networking: Networked play is essentially the same as saving a game state to the network instead of to disk, and loading from it. Thing is that once you do that, you also want to check that data for malformed data structure, value validity, game-mechanical validity, and so on. You also want to separate code that a client runs from that which a server runs (or, in the case of P2P, you want to distinguish between you and everyone else). You also want to do all of that with minimal development overhead.
  I have worked on things like that before, I have a bunch of code. But it predates WECS and has to be updated and completed.
* Modding support: I have some foggy ideas about this. Nothing concrete. But it needs to be done.
* Tons of quality-of-life improvements: Many things that went into this null project have been cobbled together hastily, and are in dire need to be improved. Every single subconsole. There isn't even a subconsole for keybindings yet. If they were worked on by people well-versed in HTML/CSS/JS, they would be powerful development tools. Other than that, WECS itself always needs more `System`s and the `Component`s that they work on, until just about every aspect of a generic game has been covered.
