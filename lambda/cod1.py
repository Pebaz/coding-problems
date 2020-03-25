"""
Question : - Given a character set [a-z] and an input as length n, print all string of length n.  

Examples :  
    
n=1, charSet[a-z]  
a
b 
c
d 
......... z


n=2, charSet[a-z]
aa
ab
ac 
ad
ae
ba
bb
bc
bd

.....
..
zz

n=3
aaa
aab
aac 
...
"""

chars = 'abcdefghijklmnopqrstuvwxyz'

# [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h'], ['i'], ['j'], ['k'], ['l'], ['m'], ['n'], ['o'], ['p'], ['q'], ['r'], ['s'],

def char_set(n: int, res: list = []) -> list:
    global chars
    
    results = []
    for i in range(n, 0, -1):
        for c in chars:
            if n != 1:
                for combo in char_set(n - 1, res + [c]):
                    results.append(combo)
            else:
                results.append(res + [c])
    return results
    

tests = []

def test(func):
    global tests
    tests.append(func)
    return func
    
def run_tests():
    for each in tests:
        failed = False
        try:
            each()
        except AssertionError:
            failed = True
        print('Test', test.__name__, 'failed' if failed else 'passed')

@test
def test_l1():
    assert char_set(1) == [
        [i] for i in chars
    ]
    
@test
def test_l2():
    gold = {
        'ur', 'nw', 'jb', 'fe', 'oi', 'tq', 'yv', 'oh', 'lu', 'ql', 'ul', 'nx',
        'xu', 'xe', 'ti', 'fp', 'yn', 'bo', 'dm', 'jw', 'jk', 'qc', 'ak', 'dz',
        'xk', 'yr', 'mp', 'ze', 'fy', 'dc', 'yq', 'nz', 'um', 'sr', 'wb', 'kx',
        'tx', 'hm', 'cb', 'lj', 'qk', 'hk', 'pt', 'tl', 'fv', 'er', 'uf', 'ui',
        'ef', 'mm', 'xy', 'rw', 'fm', 'wx', 'qw', 'xl', 'ft', 'hx', 'co', 'ka',
        'se', 'eq', 'ek', 'jc', 'mi', 'cn', 'ff', 'fz', 'hd', 'ob', 'ua', 'db',
        'pa', 'uw', 'zj', 'wc', 'vv', 'oj', 'vn', 'ba', 'vm', 'ut', 'yu', 'nm',
        'ck', 'gh', 'gj', 'pv', 'tj', 'vh', 'gr', 'qn', 'qb', 'cu', 'me', 'bf',
        'js', 'mn', 'yd', 'ap', 'vp', 'lf', 'he', 'fh', 'cz', 'le', 'ge', 'ea',
        'hq', 'yi', 'fr', 'jh', 'av', 'ed', 'xr', 'ym', 'zm', 'uk', 'qr', 'aa',
        'as', 'ev', 'nt', 'vq', 'il', 'mg', 'oy', 'nv', 'ca', 'lb', 'rt', 'vy',
        'sg', 'lk', 'td', 'eh', 'gw', 'vj', 'pm', 'gl', 'hu', 'zf', 'kj', 'ja',
        'uo', 'vl', 'vr', 'by', 'fk', 'ly', 'mu', 'qf', 'ra', 'nj', 'cd', 'et',
        'ws', 'rx', 'ta', 'fj', 'zz', 'ju', 'xp', 'ux', 'sl', 'rv', 'iz', 'ls',
        'qz', 'xj', 'kh', 'jr', 'px', 'zr', 'fn', 'bp', 'qe', 'qq', 'gb', 'dx',
        'dr', 'ip', 'hr', 'rn', 'bt', 'wv', 'sf', 'ia', 'sv', 'un', 'vt', 'iq',
        'yy', 'zi', 'pe', 'wo', 'wa', 'st', 'fb', 'cw', 'sz', 'wr', 'gu', 'go',
        'kt', 'va', 'wi', 'im', 'qh', 'up', 'vz', 'xg', 'lt', 'ij', 've', 'zl',
        'of', 'ph', 'dl', 'ud', 'wg', 'zg', 'gp', 'tr', 'ye', 'el', 'ot', 'in',
        'ko', 'jy', 'jp', 'wf', 'kk', 'kl', 'dk', 'pj', 'wq', 'ei', 'ys', 'dv',
        'vu', 'at', 'jn', 'zs', 'lo', 'lx', 'mj', 'sh', 'nc', 'nd', 'uz', 'nf',
        'od', 'az', 'cy', 'jx', 'ad', 'qo', 'yj', 'ae', 'ky', 'mb', 'pc', 'po', 
        'am', 'hn', 'tn', 'xo', 'xq', 'ns', 'ah', 'fw', 'xh', 'tg', 'oq', 'eu',
        'jt', 'uy', 'vo', 'gk', 'hp', 'hz', 'rz', 'cq', 'je', 'bk', 'lg', 'ok',
        'dw', 'ma', 'bx', 'cc', 'hj', 'fx', 'qg', 'gn', 'rl', 'on', 'qa', 'xn',
        'ie', 'ku', 'kz', 'bh', 'qt', 'yc', 'zw', 'tv', 'fl', 'ds', 'aq', 'fa',
        'ix', 'dh', 'jg', 'xd', 'ni', 'hb', 'kw', 'rh', 'yb', 'ug', 'bi', 'ir',
        'gd', 'si', 'yz', 'kf', 'rm', 'ks', 'sm', 'wm', 'sd', 'fg', 'wt', 'wu',
        'bz', 'mv', 'ml', 'gt', 'ow', 'dq', 'gm', 'op', 'jj', 'di', 'pp', 'mt',
        'pq', 'br', 'sq', 'pn', 'tk', 'cg', 'gv', 'xs', 'bg', 'we', 'pg', 'ue',
        'em', 'ld', 'ny', 'gs', 'tf', 'kn', 'vs', 'wz', 'nb', 'zy', 'eg', 'it',
        'ii', 'sn', 'al', 'ou', 'np', 'ch', 'ab', 'dg', 'qu', 'ac', 'yf', 'ww',
        'sj', 'ho', 'wk', 'lp', 'yw', 'mo', 'yl', 'bq', 'vd', 'gi', 'mw', 'lz',
        'tb', 'yt', 'sc', 'la', 'ha', 'fq', 'uc', 'uh', 'ez', 'qx', 'ps', 'nu',
        'yh', 'cr', 'cf', 'qj', 'yp', 'mh', 'ik', 'kv', 'xc', 'zv', 'jz', 'li',
        'pk', 'zx', 'zk', 'uj', 'dp', 'de', 'zu', 'ig', 'nq', 'zo', 'af', 'pd',
        'iw', 'yx', 'bd', 'my', 'ci', 'hy', 'lq', 'yo', 'en', 'ib', 'au', 'es',
        'bs', 'zp', 'og', 'us', 'wy', 'fu', 'bj', 'pi', 'ro', 'jm', 'mq', 'sp',
        'ox', 'dt', 'dy', 'rp', 'wd', 'hl', 'vk', 'pu', 'th', 'mc', 'sb', 'os',
        'xa', 'rs', 'km', 'zd', 'ax', 'hh', 'hi', 'jo', 'mf', 'gy', 'hs', 'su',
        'ki', 'tu', 'aj', 'zb', 'ey', 'om', 'ct', 'oc', 'ts', 'rr', 'ag', 'py',
        'qp', 'za', 'te', 'fo', 'xx', 'nr', 'ji', 'cs', 'mk', 'mr', 'hc', 'lv',
        'sa', 'kd', 'ss', 'jq', 'sw', 'xf', 'ry', 'bw', 'nk', 'xw', 'ai', 'ol',
        'eo', 'gf', 'vg', 'bc', 'is', 'do', 'fi', 'pf', 'du', 'tc', 'vf', 'da',
        'oz', 'rc', 'tw', 'xm', 'sy', 'pb', 'wj', 'oa', 'vc', 'wp', 'jd', 'be',
        'ke', 'hv', 'lh', 'rj', 'vx', 'lc', 'xv', 'qy', 'ew', 'ay', 'fd', 'qm',
        'so', 'id', 'bb', 'kp', 'oo', 'tp', 'zq', 'zt', 'qs', 'gx', 'jv', 'rq',
        'nh', 'ar', 'rk', 'zh', 'gq', 'ov', 'ty', 'sx', 'qv', 'to', 'tm', 'zn',
        'wh', 'yg', 'md', 'gg', 'pr', 'ln', 'dj', 'zc', 'cx', 'pz', 'tt', 'cp',
        'nn', 'pw', 'vi', 'wn', 'wl', 'ec', 'uv', 'hf', 'dn', 'ne', 'iv', 'll',
        'rd', 'rf', 'kc', 'aw', 'ej', 'ru', 'yk', 'mx', 'xz', 'oe', 'rb', 'hg',
        'uu', 'xt', 'cl', 'ng', 'hw', 'ht', 'sk', 'fc', 'jl', 'ya', 'bu', 'ep',
        'gz', 'rg', 'if', 'uq', 'bl', 'no', 'jf', 'kq', 'cj', 'cm', 'nl', 'dd',
        'qi', 're', 'lr', 'cv', 'ih', 'na', 'vb', 'an', 'tz', 'fs', 'kr', 'xi',
        'kg', 'bn', 'lm', 'or', 'ex', 'bm', 'xb', 'lw', 'ao', 'gc', 'bv', 'iy',
        'ub', 'pl', 'ms', 'qd', 'ga', 'ri', 'iu', 'io', 'kb', 'ce', 'df', 'eb',
        'ee', 'mz', 'ic', 'vw'
    }
    for combo in char_set(2):
        c = ''.join(combo)
        assert c in gold

@test
def test_l3():
    from itertools import combinations, permutations
    gold = {''.join(i) for i in combinations(chars, 3)}
    for i in permutations(chars, 3):
        gold.add(''.join(i))
    for combo in char_set(3):
        c = ''.join(combo)
        try:
            assert c in gold
        except:
            import pdb; pdb.set_trace()


if __name__ == '__main__':
    run_tests()
