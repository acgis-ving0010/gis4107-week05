def mod_sequence(seq, skip_index=None, truncate_index=None):
    modded_list = []
    for i in range(len(seq)):
        if i == skip_index:
            if i == truncate_index:
                break
            else:
                continue
        elif i == truncate_index:
            break
        else:
            modded_list.append(seq[i])
    modded_seq = ''.join(str(v) for v in modded_list)
    return modded_seq