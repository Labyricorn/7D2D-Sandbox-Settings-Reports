import os
import traceback

def lz4_decompress_safe(src, dest_len=131072):
    src_len = len(src)
    dst = bytearray()
    src_idx = 0
    try:
        while src_idx < src_len and len(dst) < dest_len:
            token = src[src_idx]
            src_idx += 1
            lit_len = token >> 4
            if lit_len == 15:
                while True:
                    if src_idx >= src_len:
                        print("lit_len overshoot src_len")
                        return None
                    s = src[src_idx]
                    src_idx += 1
                    lit_len += s
                    if s < 255:
                        break
            if src_idx + lit_len > src_len:
                print("lit copy overshoot src_len")
                return None
            dst.extend(src[src_idx : src_idx + lit_len])
            src_idx += lit_len
            if len(dst) >= dest_len or src_idx >= src_len:
                break
            if src_idx + 1 >= src_len:
                print("offset read overshoot src_len")
                return None
            offset = src[src_idx] | (src[src_idx+1] << 8)
            src_idx += 2
            if offset == 0:
                print("offset is 0")
                return None
            match_len = token & 0x0F
            if match_len == 15:
                while True:
                    if src_idx >= src_len:
                        print("match_len read overshoot src_len")
                        return None
                    s = src[src_idx]
                    src_idx += 1
                    match_len += s
                    if s < 255:
                        break
            match_len += 4
            match_idx = len(dst) - offset
            if match_idx < 0:
                print(f"match_idx {match_idx} is negative (len={len(dst)}, offset={offset})")
                return None
            for _ in range(match_len):
                if match_idx < len(dst):
                    dst.append(dst[match_idx])
                else:
                    print(f"match copy out of bounds: match_idx={match_idx}, len={len(dst)}")
                    return None
                match_idx += 1
        return bytes(dst[:dest_len])
    except Exception as e:
        print("Exception during lz4 decompress:", e)
        traceback.print_exc()
        return None

def extract():
    path = "g:/SteamLibrary/steamapps/common/7 Days To Die/7DaysToDie_Data/data.unity3d"
    f = open(path, "rb")
    
    # Block 1
    block1_offset = 29870455
    block1_comp_size = 83360
    f.seek(block1_offset)
    block1_comp_data = f.read(block1_comp_size)
    
    # Block 2
    block2_offset = block1_offset + block1_comp_size
    block2_comp_size = 93112
    f.seek(block2_offset)
    block2_comp_data = f.read(block2_comp_size)
    
    f.close()
    
    print("Decompressing Block 1...")
    res1 = lz4_decompress_safe(block1_comp_data, 131072)
    print("Block 1 result is None?", res1 is None)
    
    print("Decompressing Block 2...")
    res2 = lz4_decompress_safe(block2_comp_data, 131072)
    print("Block 2 result is None?", res2 is None)

if __name__ == "__main__":
    extract()
