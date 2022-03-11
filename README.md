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

> Note: when using this repository remember to pull in the submodule with 
> `git submodule update --init`.

One can adjust the `main.c` as one sees fit to implement their own algorithm.
Setting one of the platforms specified in the *PLATFORMS.md* in the *makefile*
will create the output files for that specified platform. By default it is set
to the `CWLITEARM`.

> Note: It is expected that both the toolchain for compiling is properly
> installed. For the ARM products this consists of the `arm-none-eabi-gcc`
> toolchain and the ARM standard library.

To run the _Python 3_ capturing code, we first need the newest version of the
ChipWhisperer python library. Then we can run `python3 capture_trace.py` in the
root directory.

## Debugging

It is possible to use `make debugging` to make *debug-target* executable with
which you can do some rough debugging. You can also check the `DEBUGGING`
constant if you want to add some conditional statement for debugging. For
example:

```c
#ifdef DEBUGGING
printf("I was here in debugging mode!\n");
#endif
```

## Contribution

If there are any issues or you can add a tested capture example for a different
platform, you can submit an issue or pull request.

## License

Licensed under a __MIT__ license.
