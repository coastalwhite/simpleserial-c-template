# Simple Serial V2 C Template

This a template repository for implementing your own SimpleSerial V2 algorithms
for execution on ChipWhisperer target boards. It comes with an example _C_ file
for our target executed binary and with an example _Python 3_ file to do our
ChipWhisperer traces. The _Python3_ code is currently only suited for the
STM32F targets, but this could easily be adjusted.

## SimpleSerial Protocol and ChipWhisperer

More info on the SimpleSerial V2 protocol can be found
[here](https://github.com/newaetech/chipwhisperer/blob/develop/hardware/victims/firmware/simpleserial/README.md).

More info on the ChipWhisperer framework can be found
[here](https://github.com/newaetech/chipwhisperer).

## Usage

One can adjust the `main.c` as one sees fit to implement their own algorithm.
Then one can compile it by running `PLATFORM={PLATFORM} SS_VER=SS_VER_2 make` in
the root directory (with `{PLATFORM}` being the target platform). One can look
in the `PLATFORMS.md` for a table provided by the ChipWhisperer framework of
supported platforms.

### Example

For the 32-bit ChipWhisperer Lite ARM-edition one would run.
```shell
PLATFORM=CWLITEARM SS_VER=SS_VER_2 make
```

To run the _Python 3_ capturing code, we first need the newest version of the
ChipWhiperer python library. Then we can run `python3 capture_trace.py` in the
root directory.

## Contribution

If there are any issues or you can add a tested capture example for a different
platform, you can submit an issue or pull request.

## License

Licensed under a __MIT__ license.
