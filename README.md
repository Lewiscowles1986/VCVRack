# Apple Silicon Support for VCV Rack Free

This is a fork of the VCV Rack v2 branch that adds the ability to compile Rack natively for Apple Silicon.

Current official releases of Rack only support targetting x86 even on Apple Silicon, in these cases Rack is run by a (very fast) emulator Rosetta 2. This emulator is very efficient and having a native port isn't really required for Rack to run on Apple Silicon devices. This repo exists because I had tried compiling natively out of interest a couple of times and each time repeated my work. I don't intend on spending much time supporting this, it's mainly for other developers to investigate Apple Silicon support rather than a product for end users.

The Rack source code and its plugins are separate, this port does not contain any plugins, they need to be ported and built separately.

An Apple Silicon build of Rack will not be able to load Mac plugins that have been built for x86.

There is a build script (./build-rack.py) that will pull some open source modules (defined in modules.json) from github and try to build them. Not all of these modules successfully compile natively for Apple Silicon. Typically if any of the module developers had gone to the effort of vectorising their modules, they won't compile without being ported to also support neon or a portable vector library like simde.
Open source plugins in the module list that I know don't compile are unfortunately:
* ValleyRackFree
* AudibleInstruments
* SquinkyVCV-main

The vector code in Rack was the main difficulty in getting it building and running, this has been patched to use the simde library.

There are a few hacks in this port that might affect the behaviour / performance:
* Floating point modes - Rack sets some floating point rounding modes in initMXCSR, this port just comments out that code in arm builds
* LuaJIT - There's some special linker commands to support this, they are also just removed in arm builds, so I imagine anything that uses LuaJIT won't work
* Non-vectorized speexdsp - This dependency doesn't support compiling for aarch64 NEON, so the --disable-neon flag has been added which I imagine means the Apple Silicon vector units are not being utilized as much as they can, hampering performance

Note that this port will also build and run for x86 like the original Rack source it's based on.

... Copy of the VCV Rack README.md follows.

# VCV Rack

*Rack* is the host application for the VCV virtual Eurorack modular synthesizer platform.

- [VCV website](https://vcvrack.com/)
- [Manual](https://vcvrack.com/manual/)
- [Support](https://vcvrack.com/support)
- [Module Library](https://library.vcvrack.com/)
- [Rack source code](https://github.com/VCVRack/Rack)
- [Building](https://vcvrack.com/manual/Building)
- [Communities](https://vcvrack.com/manual/Communities)
- [Licenses](LICENSE.md) ([HTML](LICENSE.html))

## Credits

- [Andrew Belt](https://github.com/AndrewBelt): VCV Rack developer
- [Grayscale](https://grayscale.info/): Module design, branding
- [Pyer](https://www.pyer.be/): Component graphics
- [Richie Hindle](http://entrian.com/audio/): OS/DAW-dependent bug fixes
- Christoph Scholtes: VCV Library reviews and builds
- Rack plugin developers: Authorship shown on each plugin's [VCV Library](https://library.vcvrack.com/) page
- Rack users like you: Bug reports and feature requests

## Software libraries

- [GLFW](https://www.glfw.org/)
- [GLEW](http://glew.sourceforge.net/)
- [NanoVG](https://github.com/memononen/nanovg)
- [NanoSVG](https://github.com/memononen/nanosvg)
- [oui-blendish](https://github.com/geetrepo/oui-blendish)
- [osdialog](https://github.com/AndrewBelt/osdialog) (written by Andrew Belt for VCV Rack)
- [ghc::filesystem](https://github.com/gulrak/filesystem)
- [Jansson](https://digip.org/jansson/)
- [libcurl](https://curl.se/libcurl/)
- [OpenSSL](https://www.openssl.org/)
- [Zstandard](https://facebook.github.io/zstd/) (for Rack's `tar.zstd` patch format)
- [libarchive](https://libarchive.org/) (for Rack's `tar.zstd` patch format)
- [PFFFT](https://bitbucket.org/jpommier/pffft/)
- [libspeexdsp](https://gitlab.xiph.org/xiph/speexdsp/-/tree/master/libspeexdsp) (for Rack's fixed-ratio resampler)
- [libsamplerate](https://github.com/libsndfile/libsamplerate) (for Rack's variable-ratio resampler)
- [RtMidi](https://www.music.mcgill.ca/~gary/rtmidi/)
- [RtAudio](https://www.music.mcgill.ca/~gary/rtaudio/)
- [Fuzzy Search Database](https://bitbucket.org/j_norberg/fuzzysearchdatabase) (written by Nils Jonas Norberg for VCV Rack's module browser)
- [TinyExpr](https://codeplea.com/tinyexpr) (for math evaluation in parameter context menu)

## Contributions

VCV cannot accept free contributions to Rack itself, but we encourage you to

- Send us feature requests and bug reports.
- Create a plugin that extends Rack's functionality. Most of Rack's functionality is exposed in its public plugin API.
- Work at VCV! Check job openings at <https://vcvrack.com/jobs>
