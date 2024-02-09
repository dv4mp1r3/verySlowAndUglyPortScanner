from socket_for_humans import Connection
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser("")
    parser.add_argument('-t', '--target', help="", type=str, required=True)
    args = parser.parse_args()
    print(f'Current target {args.target}')
    for i in range(1, 65535):
        try:
            addr = (args.target, i)
            cl = Connection(addr=addr, timeout=1)
            cl.close()
            print(f'\t{i} found')
        except ConnectionRefusedError:
            continue
        except Exception as e:
            print(f'Something wrong on {args.target}:{i} ({str(e)})')
            continue



