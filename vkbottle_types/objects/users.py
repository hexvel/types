from .base_model import BaseObject
from . import audio, base, account
from typing import Optional, Union, Any, List
import typing
import enum


class Career(BaseObject):
    """VK Object users/Career"""

    city_id: Optional[int] = None
    company: Optional[str] = None
    country_id: Optional[int] = None
    _from: Optional[int] = None
    group_id: Optional[int] = None
    id: Optional[int] = None
    position: Optional[str] = None
    until: Optional[int] = None


class Exports(BaseObject):
    """VK Object users/Exports"""

    facebook: Optional[int] = None
    livejournal: Optional[int] = None
    twitter: Optional[int] = None


class Fields(enum.Enum):
    """ Fields enum """

    PHOTO_ID = "photo_id"
    VERIFIED = "verified"
    SEX = "sex"
    BDATE = "bdate"
    CITY = "city"
    COUNTRY = "country"
    HOME_TOWN = "home_town"
    HAS_PHOTO = "has_photo"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_200 = "photo_200"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    ONLINE = "online"
    LISTS = "lists"
    DOMAIN = "domain"
    HAS_MOBILE = "has_mobile"
    CONTACTS = "contacts"
    SITE = "site"
    EDUCATION = "education"
    UNIVERSITIES = "universities"
    SCHOOLS = "schools"
    STATUS = "status"
    LAST_SEEN = "last_seen"
    FOLLOWERS_COUNT = "followers_count"
    COUNTERS = "counters"
    COMMON_COUNT = "common_count"
    OCCUPATION = "occupation"
    NICKNAME = "nickname"
    RELATIVES = "relatives"
    RELATION = "relation"
    PERSONAL = "personal"
    CONNECTIONS = "connections"
    EXPORTS = "exports"
    WALL_COMMENTS = "wall_comments"
    ACTIVITIES = "activities"
    INTERESTS = "interests"
    MUSIC = "music"
    MOVIES = "movies"
    TV = "tv"
    BOOKS = "books"
    GAMES = "games"
    ABOUT = "about"
    QUOTES = "quotes"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    IS_FAVORITE = "is_favorite"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    TIMEZONE = "timezone"
    SCREEN_NAME = "screen_name"
    MAIDEN_NAME = "maiden_name"
    CROP_PHOTO = "crop_photo"
    IS_FRIEND = "is_friend"
    FRIEND_STATUS = "friend_status"
    CAREER = "career"
    MILITARY = "military"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    DESCRIPTIONS = "descriptions"
    TRENDING = "trending"
    MUTUAL = "mutual"
    FRIENDSHIP_WEEKS = "friendship_weeks"
    CAN_INVITE_TO_CHATS = "can_invite_to_chats"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"


class LastSeen(BaseObject):
    """VK Object users/LastSeen"""

    platform: Optional[int] = None
    time: Optional[int] = None


class Military(BaseObject):
    """VK Object users/Military"""

    country_id: Optional[int] = None
    _from: Optional[int] = None
    id: Optional[int] = None
    unit: Optional[str] = None
    unit_id: Optional[int] = None
    until: Optional[int] = None


class Occupation(BaseObject):
    """VK Object users/Occupation"""

    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None


class OnlineInfo(BaseObject):
    """VK Object users/OnlineInfo"""

    visible: Optional[bool] = None
    last_seen: Optional[int] = None
    is_online: Optional[bool] = None
    app_id: Optional[int] = None
    is_mobile: Optional[bool] = None
    status: Optional[str] = None


class Personal(BaseObject):
    """VK Object users/Personal"""

    alcohol: Optional[int] = None
    inspired_by: Optional[str] = None
    langs: Optional[List[str]] = None
    life_main: Optional[int] = None
    people_main: Optional[int] = None
    political: Optional[int] = None
    religion: Optional[str] = None
    religion_id: Optional[int] = None
    smoking: Optional[int] = None


class Relative(BaseObject):
    """VK Object users/Relative"""

    birth_date: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None


class School(BaseObject):
    """VK Object users/School"""

    city: Optional[int] = None
    _class: Optional[str] = None
    country: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[int] = None
    type_str: Optional[str] = None
    year_from: Optional[int] = None
    year_graduated: Optional[int] = None
    year_to: Optional[int] = None


class SubscriptionsItem(BaseObject):
    """VK Object users/SubscriptionsItem"""


class University(BaseObject):
    """VK Object users/University"""

    chair: Optional[int] = None
    chair_name: Optional[str] = None
    city: Optional[int] = None
    country: Optional[int] = None
    education_form: Optional[str] = None
    education_status: Optional[str] = None
    faculty: Optional[int] = None
    faculty_name: Optional[str] = None
    graduation: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None


class User(BaseObject):
    """VK Object users/User"""


class UserConnections(BaseObject):
    """VK Object users/UserConnections"""

    skype: Optional[str] = None
    facebook: Optional[str] = None
    facebook_name: Optional[str] = None
    twitter: Optional[str] = None
    livejournal: Optional[str] = None
    instagram: Optional[str] = None


class UserCounters(BaseObject):
    """VK Object users/UserCounters"""

    albums: Optional[int] = None
    audios: Optional[int] = None
    followers: Optional[int] = None
    friends: Optional[int] = None
    gifts: Optional[int] = None
    groups: Optional[int] = None
    notes: Optional[int] = None
    online_friends: Optional[int] = None
    pages: Optional[int] = None
    photos: Optional[int] = None
    subscriptions: Optional[int] = None
    user_photos: Optional[int] = None
    user_videos: Optional[int] = None
    videos: Optional[int] = None


class UserFull(BaseObject):
    """VK Object users/UserFull"""


class UserMin(BaseObject):
    """VK Object users/UserMin"""

    deactivated: Optional[str] = None
    first_name: Optional[str] = None
    hidden: Optional[int] = None
    id: Optional[int] = None
    last_name: Optional[str] = None
    can_access_closed: Optional[bool] = None
    is_closed: Optional[bool] = None


class UserRelation(enum.IntEnum):
    """ UserRelation enum """

    not_specified = 0
    single = 1
    in_a_relationship = 2
    engaged = 3
    married = 4
    complicated = 5
    actively_searching = 6
    in_love = 7
    in_a_civil_union = 8


class UserSettingsXtr(BaseObject):
    """VK Object users/UserSettingsXtr"""

    connections: Optional["UserConnections"]
    bdate: Optional[str] = None
    bdate_visibility: Optional[int] = None
    city: Optional[base.City] = None
    country: Optional[base.Country] = None
    first_name: Optional[str] = None
    home_town: Optional[str] = None
    last_name: Optional[str] = None
    maiden_name: Optional[str] = None
    name_request: Optional[account.NameRequest] = None
    personal: Optional["Personal"]
    phone: Optional[str] = None
    relation: Optional["UserRelation"]
    relation_partner: Optional["UserMin"]
    relation_pending: Optional[base.BoolInt] = None
    relation_requests: Optional[List["UserMin"]]
    screen_name: Optional[str] = None
    sex: Optional[base.Sex] = None
    status: Optional[str] = None
    status_audio: Optional[audio.Audio] = None
    interests: Optional[account.UserSettingsInterests] = None
    languages: Optional[List[str]] = None


class UserType(enum.Enum):
    """ Object type """

    PROFILE = "profile"


class UserXtrCounters(BaseObject):
    """VK Object users/UserXtrCounters"""


class UserXtrType(BaseObject):
    """VK Object users/UserXtrType"""


class UsersArray(BaseObject):
    """VK Object users/UsersArray"""

    count: Optional[int] = None
    items: Optional[List[int]] = None
