import sys
import typing


def action_sanitize():
    ''' Make action suitable for use as a Pose Library

    '''

    pass


def apply_pose(pose_index: int = -1):
    ''' Apply specified Pose Library pose to the rig

    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: int
    '''

    pass


def browse_interactive(pose_index: int = -1):
    ''' Interactively browse poses in 3D-View

    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: int
    '''

    pass


def new():
    ''' Add New Pose Library to active Object

    '''

    pass


def pose_add(frame: int = 1, name: str = "Pose"):
    ''' Add the current Pose to the active Pose Library

    :param frame: Frame, Frame to store pose on
    :type frame: int
    :param name: Pose Name, Name of newly added Pose
    :type name: str
    '''

    pass


def pose_move(pose: typing.Union[str, int] = '',
              direction: typing.Union[str, int] = 'UP'):
    ''' Move the pose up or down in the active Pose Library

    :param pose: Pose, The pose to move
    :type pose: typing.Union[str, int]
    :param direction: Direction, Direction to move the chosen pose towards
    :type direction: typing.Union[str, int]
    '''

    pass


def pose_remove(pose: typing.Union[str, int] = ''):
    ''' Remove nth pose from the active Pose Library

    :param pose: Pose, The pose to remove
    :type pose: typing.Union[str, int]
    '''

    pass


def pose_rename(name: str = "RenamedPose", pose: typing.Union[str, int] = ''):
    ''' Rename specified pose from the active Pose Library

    :param name: New Pose Name, New name for pose
    :type name: str
    :param pose: Pose, The pose to rename
    :type pose: typing.Union[str, int]
    '''

    pass


def unlink():
    ''' Remove Pose Library from active Object

    '''

    pass
