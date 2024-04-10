wecs_null_project
=================

You want to develop a game, using Python, Panda3D, and WECS? You don't
want to write all the stuff that every game has to have? You want to get
working on what makes your game *your* game? **Now**?

Well, then do!


But I don't know...
-------------------

### Python

It's a popular and easy to learn programming language, and, dare I say
it, aesthetically pleasing. You can install it via your platform's
package manager, or from https://www.python.org/ where you also find the
official documentation, including a tutorial. If that's not your
preferred way of learning, there's hundreds of courses, tutorials, every
kind of resource imaginable.


### Panda3D

Panda3D is a 3D engine that is used most often for games, but has also
been used for engineering and visualization applications, art
installations, amusement park rides, amusement park ride design, ...

Originally developed by Disney, it has been open sourced, and is now
developed by its community. Despite rumors to the contrary, it is very
much alive and close to the state of the art of graphics technology.

Panda3D can be used with Python or C++. If C++ is your thing, I'm afraid
that this boilerplate project is not for you, it's aimed at Python
developers.

Unlike popular 3D engines, Panda3D does *not* come with an interactive
game creation and editing toolchain. It is a library that offers you
lots and lots of tools and building blocks, but you have to string them
together with code. The reasoning is that any editor would make
assumptions about how a game should be structured, limiting the design
space of its user. Since flexibility is very high on the priority list
of Panda3D development, designing an editor is a task that so far has
not been tackled with confidence.

Model assets for Panda3D are usually created with Blender, though
converters for other formats do exist, and Panda3D also reads glTF,
which may become the de facto standard in the near future. Sound assets
can be used as long as FFMPEG can read them.

You can find further information at https://www.panda3d.org/


### WECS

WECS is a set of strong assumptions about how a game should be
structured, usually called ECS, "Entity, Component, System", or
"Component System". Specifically, it assumes (and implements) these
ideas:

* A game object, called an `Entity`, consists of a set of `Components`,
  and nothing more.
* Each `Component` describes the state of the `Entity` with regard to
  some aspect of its existence. A `Component` only stores data. It does
  not implement any functionality to manipulate that data.
* For each tick / frame of the game, there is a list of `System`s that
  are run in order. Consider them as a kind of Panda3D `Task`.
  * Each `System` has a set (actually a dictionary in code) of
    `entity_filters` that specify what `Component`s an `Entity` has to
    have to be processed.
  * When a `System` is being run, it receives a list of `Entity`s for
    each `entity_filter`, which contain all `Entity`s that match a given
    `entity_filter`.

This is an approach to game architecture that allows both a high degree
of flexibility, and keeps each `System` manageably simple and isolated
from other `System`s. That means less effort to maintain code, and that
it is easy to combine separately developed game mechanics in the the
same game. That also means that WECS can contain a lot of pre-made
`System`s and `Component`s that you can just plug into your game.

Further information: [GitHub](https://github.com/TheCheapestPixels/wecs)


### panda3d-stageflow

You know how games have splash screens, an introductory cutscene, the
main menu, the main game loop, more cutscenes, ingame menus, settings
menus, keybindings menus, screens for saving games, loading games, and
so on and on, and how it is all a chore to keep it all manageable?

`panda3d-stageflow` does just that. The game moves from stage to stage,
which are the major states of the game (main menu, main loop), and the
game is always in exactly one of them. There are also substages, which
can be added as a stack on top of the stages, and which usually
structure menus.

Further information: [GitHub](https://github.com/TheCheapestPixels/panda3d-stageflow)


### panda3d-keybindings

Panda3D... has systems to work with user inputs. They are quite a long
way away from what you are expecting from a game, namely a keybindings
menu and no further worries. `panda3d-keybindings` is an ongoing effort
to close the gap. Its current state is that there is
`keybindings.config`, a structured file file for defining contexts in
which keybindings can exist, what kind of bindings they are (button,
triggers, 3D axis, etc.) and what their names are, and to which input
methods they map. As you can see in the file, only the debug bindings
are currently present.

Further information: [GitHub](https://github.com/TheCheapestPixels/panda3d-keybindings)


Let's get going!
----------------

Now that you know the tech stack with which we will be working, let's
get the show on the road!


### Setting up the development environment

1. Copy this project's files.
2. Install its requirements: `pip install -r requirements.txt`
3. Run `main.py`.

You should be treated to the Panda3D splash screen, after which you will
unceremoniously be dropped into a blank blue screen. You can use
`escape` to skip the former and exit the game while in the latter.


### Overview of the present state

Everything good so far? Then you're ready for development. You should
now have a game with...

* a basic stage flow that...
  * is set up in `game/__init__.py`
  * also has an entry point for development which skips the splashes,
    and is used by starting the game with
    `python main.py --stage debug`,
* a `WECS` world at `base.ecs_world`
* the `panda3d-keybindings` device listener, configured in
  `keybindings.config`,
* the `MainGameLoop` stage, which...
  * has one `System`, `wecs.panda3d.debug.DebugTools`, providing debug
    keys that by default are mapped to...
    * `escape` to exit the game (via `sys.exit()`)
    * `f10`: toggle the frame rate meter
    * `f11`: drop into a pdb session
    * `f12`: connect to the `pstats` server
  * no entities
  * is defined in `game/main_loop.py`

You can home in further on your prototype by adding premade systems that
ship with WECS, and now you *really* should be ready to implement your
own mechanics.
CAVEAT: I'm not happy at all with WECS' standard library of generic
mechanics yet...


### Deployment

As fun as game development for the sake of it can be, usually it is also
for the sake of shipping a game. To do that, we again have to do a bunch
of paperwork first:

1. Go through `setup.py` and change the lines marked with the comment
   `# STARTPROJECT` to reflect your game.
1. Rewrite this README.md from scratch, and add your preferred licensing
   conditions to LICENSE.
1. Run `python setup.py bdist_apps` to build distributable packages, and
   test them.
   CAVEAT: Still buggy. Sorry.
   NOTE: You can run `python setup.py build_apps` to build your project
   without packaging it. This is faster, and allows you check whether a
   bug occurs due to building alone, or due to packaging.


### Done!

That's it already: Plug together all the things that you have and need,
then write the ones that you don't have, but need. Develop, test, build,
distribute, done.


Coming soon(-ish)
-----------------

As you saw in the introductory section, things are... not quite ready
for prime time. There's one problem with this project itself right now:

* Deployment: I'm pushing that one forward one bug at a time...

There's also a few major features missing in my software toolbelt to
consider things ready for said prime time:

* Loading / saving games: There's no automatism yet to serialize the
  state of all `Component`s in the world that should be saved). Once
  that (and the corresponding deserialization) is added, saving and
  loading a game state should be a breeze.
* Networking: Networked play is essentially the same as saving a game
  state to the network instead of to disk, and loading from it. Thing is
  that once you do that, you also want to check that data for malformed
  data structure, value validity, game-mechanical validity, and so on.
  You also want to separate code that a client runs from that which a
  server runs (or, in the case of P2P, you want to distinguish between
  you and everyone else). You also want to do all of that with minimal
  development overhead.
  
  I have worked on things like that before, I have a bunch of code. But
  it predates WECS and has to be updated and completed.
* Modding support: I have some foggy ideas about this. Nothing concrete.
  But it needs to be done.
* GUI and game spec files: We need a bunch of consoles, in particular a
  Python REPL, an overview over systems and entities, and one to edit
  entities. Premade WECS mechanics should also have tools. Since there
  are now a lot of strong assumptions, editors become possible, and
  their state can be saved and loaded. This means that eventually, any
  work that doesn't involve writing new mechanics can be done
  graphically.

And finally, there's a few documentation issue. `wecs_null_project`
draws upon lots of projects:
* `panda3d-stageflow`: Coarse game structure
* `panda3d-logos`: Contains Panda3D splash screen stage
* `wecs`: Gameplay
* `panda3d-keybindings`: Easier input management and keybinding files
* `panda3d-gltf`: Let Panda3D read glTF
* `blend2bam`: Another way to get assets from Blender into Panda3D
* `panda3d-simplepbr`: Physics-based rendering
* `pman`: CAVEAT: Nothing yet, but eventually, I want `pman init wecs`
  
Each of them should be documented well individually; Also, there should
be a unified tutorial showing how they interact. Revamping the Pong
example would be a good start.

In conclusion and repetition, `wecs_null_project` isn't ready for prime
time, meaning that it (or rather, many of the projects it uses) doesn't
*yet* do what aims to do: Making the creation and deployment of a
generic game a matter of five minutes. What is there so far however
demonstrates that with enough development effort, this is a perfectly
achievable goal.


Thanks
------

Thank you to...
* Entikan, for being an all-around great guy and motivator.
* Simulan, for critical help with getting deployment going.
* rdb and all Panda3D committers, for making Panda3D not just survive,
  but thrive.


TODO
----

FIXME: Why do I rely on a local argparser that does not even know about
data being passed to it?
