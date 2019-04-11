import json, os, sys
import numpy as np

def pack(input_path, output_path):
    output = {}
    for var in ['test', 'train', 'valid']:
        output[var] = []
        p = input_path + '/' + var
        for i in os.listdir(p):
            if i.endswith('.json'):
                full_path = '%s/%s' % (p, i)
                with open(full_path) as f:
                    data = json.load(f)
                    if len(data) > 0:
                        strokes = []
                        for d in data:
                            stroke = []
                            for s in [0,1,3]:
                                stroke.append(d[s])
                            strokes.append(stroke)
                        t = np.array(strokes, dtype='int16')
                        output[var].append(t)
    p = output_path + '/' + 'output.npz'
    np.savez_compressed(p, test=output['test'], train=output['train'], valid=output['valid'])
    return True

if __name__ == '__main__':
    if pack(sys.argv[1], sys.argv[2]):
        print('complete!')
