# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A Python library (`rwclib`) that controls an RWC5020A/B/M LoRaWAN tester through its remote-command interface, over RS-232 or Ethernet (TCP, usually port 5001). Each library method sends one SCPI-style command (`CONF:...`, `READ:...?`, `EXEC:...`) and returns the tester's reply: `ACK`, `NAK`, or the value queried.

- `rwclib/cRWCSerialSetup.py`: `RwcSerialSetup`, the transport (`open_port()`, `transceive()`, `close_port()`).
- `rwclib/cRWC5020x.py`: `RWCTesterApi(port, addr=None)`, one method per tester command, about 11,000 lines. Methods are grouped by prefix: `query_*`, `rf_*`, `protocol_*`, `link_*`, `nst_tx_*`, `nst_rx_*`, `nst_mfg_*`.
- `examples/`: scripts that set up the tester and run parts of the EU certification tests.
- `tests/test_commands.py`: offline pytest tests that check the command strings methods send, with a stand-in for `transceive()`. Run `uv run --with pytest --with pyserial python -m pytest tests/test_commands.py`. Add a test with each fix.
- `tests/rwc5020x_test_*.py`: one `unittest` file per tester firmware version (`rwc5020x_test_1_31.py` is v1.310), run as `python rwc5020x_test_1_31.py <serial-port>`. They need a tester on a serial port and change its setup.
- `doc/build/html/`: generated API documentation (Sphinx); the sources are not in the repository.

## Using it

```python
import sys; sys.path.insert(0, '<repo>')
from rwclib.cRWC5020x import RWCTesterApi
from rwclib.cRWCSerialSetup import RwcSerialSetup

t = RWCTesterApi('5001', '192.168.1.16')    # Ethernet: port, then address
t.open_port()
t.query_sysversion()                          # '1.500'
RwcSerialSetup.transceive(t, 'READ:NST:TX:SYNC_WORD?\n')   # any command the library lacks
t.close_port()
```

## Conventions and pitfalls

- **Firmware versions.** Commands change between tester firmware releases. Use `require_swversion(since=..., before=...)` for a command that exists only in a range of firmware versions, and `swversion_number()` to choose between old and new forms of a command. Don't check against a list of version strings (`validate_sys_swversion()`, now unused); a list goes stale with each new firmware release. The firmware's revision history in the operation manual says when each command was added or deleted.
- **Queries** use `READ:...?`. Firmware 1.500 NAKs `CONF:...?`.
- **Hex values** (sync words, payloads) go through `_hexparam()`, which takes bytes, a hex string starting with `0x`, an int, or a decimal string. A plain string is decimal because v1.0.4 read it that way; don't change that, since a caller's payload would change with no error. The tester NAKs a payload whose length differs from the payload size, and does not pad short values.
- **Restore the tester.** Changing NST or protocol settings changes the tester for everyone using it. Read each value before changing it and set it back afterwards; stop the link (`EXEC:LINK:STOP`) before changing modes and restart it (`EXEC:LINK:RUN`) when done.
- **Logging.** The library logs through `logging.getLogger(__name__)` and leaves handlers and levels to the application.
- New methods follow the existing pattern: a docstring with `:param:` and `:return:`, build the command string, call `RwcSerialSetup.transceive()`, raise `Exception('Invalid parameter received.')` for bad arguments.

## Releases

A release advances the version in `VERSION.txt` (`v1.0.5`), `setup.py`, and the README's Release History, and is tagged `v<version>` after merging. Every PR that changes the library advances the version. Default branch: `master`.
