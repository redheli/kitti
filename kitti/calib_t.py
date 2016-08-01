"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class calib_t(object):
    __slots__ = ["utime", "K_cam_left", "K_cam_right", "cam_left_imu", "cam_right_imu", "cam_left_velo", "cam_right_velo", "velo_imu"]

    def __init__(self):
        self.utime = 0
        self.K_cam_left = [ [ 0.0 for dim1 in range(3) ] for dim0 in range(3) ]
        self.K_cam_right = [ [ 0.0 for dim1 in range(3) ] for dim0 in range(3) ]
        self.cam_left_imu = [ [ 0.0 for dim1 in range(4) ] for dim0 in range(4) ]
        self.cam_right_imu = [ [ 0.0 for dim1 in range(4) ] for dim0 in range(4) ]
        self.cam_left_velo = [ [ 0.0 for dim1 in range(4) ] for dim0 in range(4) ]
        self.cam_right_velo = [ [ 0.0 for dim1 in range(4) ] for dim0 in range(4) ]
        self.velo_imu = [ [ 0.0 for dim1 in range(4) ] for dim0 in range(4) ]

    def encode(self):
        buf = BytesIO()
        buf.write(calib_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.utime))
        for i0 in range(3):
            buf.write(struct.pack('>3d', *self.K_cam_left[i0][:3]))
        for i0 in range(3):
            buf.write(struct.pack('>3d', *self.K_cam_right[i0][:3]))
        for i0 in range(4):
            buf.write(struct.pack('>4d', *self.cam_left_imu[i0][:4]))
        for i0 in range(4):
            buf.write(struct.pack('>4d', *self.cam_right_imu[i0][:4]))
        for i0 in range(4):
            buf.write(struct.pack('>4d', *self.cam_left_velo[i0][:4]))
        for i0 in range(4):
            buf.write(struct.pack('>4d', *self.cam_right_velo[i0][:4]))
        for i0 in range(4):
            buf.write(struct.pack('>4d', *self.velo_imu[i0][:4]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != calib_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return calib_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = calib_t()
        self.utime = struct.unpack(">q", buf.read(8))[0]
        self.K_cam_left = []
        for i0 in range(3):
            self.K_cam_left.append(struct.unpack('>3d', buf.read(24)))
        self.K_cam_right = []
        for i0 in range(3):
            self.K_cam_right.append(struct.unpack('>3d', buf.read(24)))
        self.cam_left_imu = []
        for i0 in range(4):
            self.cam_left_imu.append(struct.unpack('>4d', buf.read(32)))
        self.cam_right_imu = []
        for i0 in range(4):
            self.cam_right_imu.append(struct.unpack('>4d', buf.read(32)))
        self.cam_left_velo = []
        for i0 in range(4):
            self.cam_left_velo.append(struct.unpack('>4d', buf.read(32)))
        self.cam_right_velo = []
        for i0 in range(4):
            self.cam_right_velo.append(struct.unpack('>4d', buf.read(32)))
        self.velo_imu = []
        for i0 in range(4):
            self.velo_imu.append(struct.unpack('>4d', buf.read(32)))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if calib_t in parents: return 0
        tmphash = (0xa78d28424b63af08) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if calib_t._packed_fingerprint is None:
            calib_t._packed_fingerprint = struct.pack(">Q", calib_t._get_hash_recursive([]))
        return calib_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

