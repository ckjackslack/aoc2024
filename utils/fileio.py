def read_line_by_line(filepath, strip=False, skip_empty=False):
    with open(filepath) as f:
        for line in f:
            ret = line
            if strip:
                ret = ret.strip()
            if skip_empty and not ret:
                continue
            yield ret
