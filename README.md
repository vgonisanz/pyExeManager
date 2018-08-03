# pyExeManager

Sample to manage a binary using python under GNU LGPL v3.0 license.

**pyExeManager** is compatible with Python-3.5 and greater versions.

# Using

Clone the repository:

```
$ git clone git@github.com:vgonisanz/pyExeManager.git
```

Execute basic sample:

```
$ cd samples
$ python3 basic.py
```

# What is this example intended for?

This should be used as an example to manage a binary. In this case,
`bin/playersample` is used. It is a simple menu that expect user
inputs. It require to execute `libcore.so` included too in the bin
folder. It was compile in a x64 Linux machine.

The complete info from the binary can be extracted using `objdump`:

```
$ objdump -p playersample

playersample:     file format elf64-x86-64

Program Header:
    PHDR off    0x0000000000000040 vaddr 0x0000000000400040 paddr 0x0000000000400040 align 2**3
         filesz 0x00000000000001f8 memsz 0x00000000000001f8 flags r-x
  INTERP off    0x0000000000000238 vaddr 0x0000000000400238 paddr 0x0000000000400238 align 2**0
         filesz 0x000000000000001c memsz 0x000000000000001c flags r--
    LOAD off    0x0000000000000000 vaddr 0x0000000000400000 paddr 0x0000000000400000 align 2**21
         filesz 0x000000000000cf0c memsz 0x000000000000cf0c flags r-x
    LOAD off    0x000000000000dcd0 vaddr 0x000000000060dcd0 paddr 0x000000000060dcd0 align 2**21
         filesz 0x000000000000045c memsz 0x0000000000000520 flags rw-
 DYNAMIC off    0x000000000000ddd0 vaddr 0x000000000060ddd0 paddr 0x000000000060ddd0 align 2**3
         filesz 0x0000000000000220 memsz 0x0000000000000220 flags rw-
    NOTE off    0x0000000000000254 vaddr 0x0000000000400254 paddr 0x0000000000400254 align 2**2
         filesz 0x0000000000000044 memsz 0x0000000000000044 flags r--
EH_FRAME off    0x000000000000aea0 vaddr 0x000000000040aea0 paddr 0x000000000040aea0 align 2**2
         filesz 0x00000000000005f4 memsz 0x00000000000005f4 flags r--
   STACK off    0x0000000000000000 vaddr 0x0000000000000000 paddr 0x0000000000000000 align 2**4
         filesz 0x0000000000000000 memsz 0x0000000000000000 flags rw-
   RELRO off    0x000000000000dcd0 vaddr 0x000000000060dcd0 paddr 0x000000000060dcd0 align 2**0
         filesz 0x0000000000000330 memsz 0x0000000000000330 flags r--

Dynamic Section:
  NEEDED               libcore.so
  NEEDED               libstdc++.so.6
  NEEDED               libm.so.6
  NEEDED               libgcc_s.so.1
  NEEDED               libc.so.6
  RPATH                /home/vgoni/Work/Personal/git/memdynedition/build/bin:
  INIT                 0x0000000000407700
  FINI                 0x000000000040ab94
  INIT_ARRAY           0x000000000060dcd0
  INIT_ARRAYSZ         0x0000000000000010
  FINI_ARRAY           0x000000000060dce0
  FINI_ARRAYSZ         0x0000000000000008
  GNU_HASH             0x0000000000400298
  STRTAB               0x0000000000402648
  SYMTAB               0x0000000000400ad0
  STRSZ                0x0000000000004a07
  SYMENT               0x0000000000000018
  DEBUG                0x0000000000000000
  PLTGOT               0x000000000060e000
  PLTRELSZ             0x0000000000000330
  PLTREL               0x0000000000000007
  JMPREL               0x00000000004073d0
  RELA                 0x0000000000407340
  RELASZ               0x0000000000000090
  RELAENT              0x0000000000000018
  VERNEED              0x00000000004072a0
  VERNEEDNUM           0x0000000000000003
  VERSYM               0x0000000000407050

Version References:
  required from libgcc_s.so.1:
    0x0b792650 0x00 08 GCC_3.0
  required from libc.so.6:
    0x09691a75 0x00 04 GLIBC_2.2.5
  required from libstdc++.so.6:
    0x0bafd179 0x00 07 CXXABI_1.3.9
    0x056bafd3 0x00 06 CXXABI_1.3
    0x08922974 0x00 05 GLIBCXX_3.4
    0x0297f869 0x00 03 GLIBCXX_3.4.19
    0x0297f871 0x00 02 GLIBCXX_3.4.21
```

If you have problem with the binary, you can compile it cloning the code
from [this other](https://github.com/vgonisanz/memdynedition) repository.
