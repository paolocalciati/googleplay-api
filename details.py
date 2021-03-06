##
## Basic script to retrieve the public details of an app.
## author: Alessandra Gorla
##

#!/usr/bin/python

#!/usr/bin/python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

VALID_PERMISSIONS = ['android.permission.WRITE_SETTINGS', 'android.permission.READ_CONTACTS', 'android.permission.WRITE_CONTACTS', 'android.permission.READ_CALENDAR', 'android.permission.WRITE_CALENDAR', 'android.permission.SEND_SMS', 'android.permission.RECEIVE_SMS', 'android.permission.READ_SMS', 'android.permission.RECEIVE_WAP_PUSH', 'android.permission.RECEIVE_MMS', 'android.permission.READ_CELL_BROADCASTS', 'android.permission.READ_EXTERNAL_STORAGE', 'android.permission.WRITE_EXTERNAL_STORAGE', 'android.permission.ACCESS_FINE_LOCATION', 'android.permission.ACCESS_COARSE_LOCATION', 'android.permission.READ_PHONE_STATE', 'android.permission.CALL_PHONE', 'android.permission.ACCESS_IMS_CALL_SERVICE', 'android.permission.READ_CALL_LOG', 'android.permission.WRITE_CALL_LOG', 'android.permission.ADD_VOICEMAIL', 'android.permission.USE_SIP', 'android.permission.PROCESS_OUTGOING_CALLS', 'android.permission.RECORD_AUDIO', 'android.permission.CAMERA', 'android.permission.BODY_SENSORS', 'android.permission.USE_FINGERPRINT', 'android.permission.READ_PROFILE', 'android.permission.WRITE_PROFILE', 'android.permission.READ_SOCIAL_STREAM', 'android.permission.WRITE_SOCIAL_STREAM', 'android.permission.READ_USER_DICTIONARY', 'android.permission.WRITE_USER_DICTIONARY', 'android.permission.WRITE_SMS', 'android.permission.READ_HISTORY_BOOKMARKS', 'android.permission.WRITE_HISTORY_BOOKMARKS', 'android.permission.AUTHENTICATE_ACCOUNTS', 'android.permission.MANAGE_ACCOUNTS', 'android.permission.USE_CREDENTIALS', 'android.permission.SUBSCRIBED_FEEDS_READ', 'android.permission.SUBSCRIBED_FEEDS_WRITE', 'android.permission.SEND_RESPOND_VIA_MESSAGE', 'android.permission.CARRIER_FILTER_SMS', 'android.permission.RECEIVE_EMERGENCY_BROADCAST', 'android.permission.RECEIVE_BLUETOOTH_MAP', 'android.permission.BIND_DIRECTORY_SEARCH', 'android.permission.MODIFY_CELL_BROADCASTS', 'android.permission.SET_ALARM', 'android.permission.WRITE_VOICEMAIL', 'android.permission.READ_VOICEMAIL', 'android.permission.ACCESS_LOCATION_EXTRA_COMMANDS', 'android.permission.INSTALL_LOCATION_PROVIDER', 'android.permission.HDMI_CEC', 'android.permission.LOCATION_HARDWARE', 'android.permission.ACCESS_MOCK_LOCATION', 'android.permission.INTERNET', 'android.permission.ACCESS_NETWORK_STATE', 'android.permission.ACCESS_WIFI_STATE', 'android.permission.CHANGE_WIFI_STATE', 'android.permission.READ_WIFI_CREDENTIAL', 'android.permission.RECEIVE_WIFI_CREDENTIAL_CHANGE', 'android.permission.OVERRIDE_WIFI_CONFIG', 'android.permission.ACCESS_WIMAX_STATE', 'android.permission.CHANGE_WIMAX_STATE', 'android.permission.SCORE_NETWORKS', 'android.permission.BLUETOOTH', 'android.permission.BLUETOOTH_ADMIN', 'android.permission.BLUETOOTH_PRIVILEGED', 'android.permission.BLUETOOTH_MAP', 'android.permission.BLUETOOTH_STACK', 'android.permission.NFC', 'android.permission.CONNECTIVITY_INTERNAL', 'android.permission.PACKET_KEEPALIVE_OFFLOAD', 'android.permission.RECEIVE_DATA_ACTIVITY_CHANGE', 'android.permission.LOOP_RADIO', 'android.permission.NFC_HANDOVER_STATUS', 'android.permission.GET_ACCOUNTS', 'android.permission.ACCOUNT_MANAGER', 'android.permission.CHANGE_WIFI_MULTICAST_STATE', 'android.permission.VIBRATE', 'android.permission.FLASHLIGHT', 'android.permission.WAKE_LOCK', 'android.permission.TRANSMIT_IR', 'android.permission.MODIFY_AUDIO_SETTINGS', 'android.permission.MANAGE_USB', 'android.permission.ACCESS_MTP', 'android.permission.HARDWARE_TEST', 'android.permission.ACCESS_FM_RADIO', 'android.permission.NET_ADMIN', 'android.permission.REMOTE_AUDIO_PLAYBACK', 'android.permission.TV_INPUT_HARDWARE', 'android.permission.CAPTURE_TV_INPUT', 'android.permission.DVB_DEVICE', 'android.permission.OEM_UNLOCK_STATE', 'android.permission.ACCESS_PDB_STATE', 'android.permission.NOTIFY_PENDING_SYSTEM_UPDATE', 'android.permission.CAMERA_DISABLE_TRANSMIT_LED', 'android.permission.CAMERA_SEND_SYSTEM_EVENTS', 'android.permission.MODIFY_PHONE_STATE', 'android.permission.READ_PRECISE_PHONE_STATE', 'android.permission.READ_PRIVILEGED_PHONE_STATE', 'android.permission.REGISTER_SIM_SUBSCRIPTION', 'android.permission.REGISTER_CALL_PROVIDER', 'android.permission.REGISTER_CONNECTION_MANAGER', 'android.permission.BIND_INCALL_SERVICE', 'android.permission.BIND_CONNECTION_SERVICE', 'android.permission.BIND_TELECOM_CONNECTION_SERVICE', 'android.permission.CONTROL_INCALL_EXPERIENCE', 'android.permission.RECEIVE_STK_COMMANDS', 'android.permission.WRITE_MEDIA_STORAGE', 'android.permission.MANAGE_DOCUMENTS', 'android.permission.DISABLE_KEYGUARD', 'android.permission.GET_TASKS', 'android.permission.REAL_GET_TASKS', 'android.permission.START_TASKS_FROM_RECENTS', 'android.permission.INTERACT_ACROSS_USERS', 'android.permission.INTERACT_ACROSS_USERS_FULL', 'android.permission.MANAGE_USERS', 'android.permission.MANAGE_PROFILE_AND_DEVICE_OWNERS', 'android.permission.GET_DETAILED_TASKS', 'android.permission.REORDER_TASKS', 'android.permission.REMOVE_TASKS', 'android.permission.MANAGE_ACTIVITY_STACKS', 'android.permission.START_ANY_ACTIVITY', 'android.permission.RESTART_PACKAGES', 'android.permission.KILL_BACKGROUND_PROCESSES', 'android.permission.GET_PACKAGE_IMPORTANCE', 'android.permission.SYSTEM_ALERT_WINDOW', 'android.permission.SET_WALLPAPER', 'android.permission.SET_WALLPAPER_HINTS', 'android.permission.SET_TIME', 'android.permission.SET_TIME_ZONE', 'android.permission.EXPAND_STATUS_BAR', 'android.permission.INSTALL_SHORTCUT', 'android.permission.UNINSTALL_SHORTCUT', 'android.permission.READ_SYNC_SETTINGS', 'android.permission.WRITE_SYNC_SETTINGS', 'android.permission.READ_SYNC_STATS', 'android.permission.SET_SCREEN_COMPATIBILITY', 'android.permission.CHANGE_CONFIGURATION', 'android.permission.WRITE_SETTINGS', 'android.permission.WRITE_GSERVICES', 'android.permission.FORCE_STOP_PACKAGES', 'android.permission.RETRIEVE_WINDOW_CONTENT', 'android.permission.SET_ANIMATION_SCALE', 'android.permission.PERSISTENT_ACTIVITY', 'android.permission.GET_PACKAGE_SIZE', 'android.permission.SET_PREFERRED_APPLICATIONS', 'android.permission.RECEIVE_BOOT_COMPLETED', 'android.permission.BROADCAST_STICKY', 'android.permission.MOUNT_UNMOUNT_FILESYSTEMS', 'android.permission.MOUNT_FORMAT_FILESYSTEMS', 'android.permission.ASEC_ACCESS', 'android.permission.ASEC_CREATE', 'android.permission.ASEC_DESTROY', 'android.permission.ASEC_MOUNT_UNMOUNT', 'android.permission.ASEC_RENAME', 'android.permission.WRITE_APN_SETTINGS', 'android.permission.CHANGE_NETWORK_STATE', 'android.permission.CLEAR_APP_CACHE', 'android.permission.ALLOW_ANY_CODEC_FOR_PLAYBACK', 'android.permission.MANAGE_CA_CERTIFICATES', 'android.permission.RECOVERY', 'android.permission.BIND_JOB_SERVICE', 'android.permission.UPDATE_CONFIG', 'android.permission.WRITE_SECURE_SETTINGS', 'android.permission.DUMP', 'android.permission.READ_LOGS', 'android.permission.SET_DEBUG_APP', 'android.permission.SET_PROCESS_LIMIT', 'android.permission.SET_ALWAYS_FINISH', 'android.permission.SIGNAL_PERSISTENT_PROCESSES', 'android.permission.GET_ACCOUNTS_PRIVILEGED', 'android.permission.DIAGNOSTIC', 'android.permission.STATUS_BAR', 'android.permission.STATUS_BAR_SERVICE', 'android.permission.FORCE_BACK', 'android.permission.UPDATE_DEVICE_STATS', 'android.permission.GET_APP_OPS_STATS', 'android.permission.UPDATE_APP_OPS_STATS', 'android.permission.INTERNAL_SYSTEM_WINDOW', 'android.permission.MANAGE_APP_TOKENS', 'android.permission.FREEZE_SCREEN', 'android.permission.INJECT_EVENTS', 'android.permission.FILTER_EVENTS', 'android.permission.RETRIEVE_WINDOW_TOKEN', 'android.permission.FRAME_STATS', 'android.permission.TEMPORARY_ENABLE_ACCESSIBILITY', 'android.permission.SET_ACTIVITY_WATCHER', 'android.permission.SHUTDOWN', 'android.permission.STOP_APP_SWITCHES', 'android.permission.GET_TOP_ACTIVITY_INFO', 'android.permission.READ_INPUT_STATE', 'android.permission.BIND_INPUT_METHOD', 'android.permission.BIND_MIDI_DEVICE_SERVICE', 'android.permission.BIND_ACCESSIBILITY_SERVICE', 'android.permission.BIND_PRINT_SERVICE', 'android.permission.BIND_NFC_SERVICE', 'android.permission.BIND_PRINT_SPOOLER_SERVICE', 'android.permission.BIND_TEXT_SERVICE', 'android.permission.BIND_VPN_SERVICE', 'android.permission.BIND_WALLPAPER', 'android.permission.BIND_VOICE_INTERACTION', 'android.permission.MANAGE_VOICE_KEYPHRASES', 'android.permission.BIND_REMOTE_DISPLAY', 'android.permission.BIND_TV_INPUT', 'android.permission.MODIFY_PARENTAL_CONTROLS', 'android.permission.BIND_ROUTE_PROVIDER', 'android.permission.BIND_DEVICE_ADMIN', 'android.permission.MANAGE_DEVICE_ADMINS', 'android.permission.SET_ORIENTATION', 'android.permission.SET_POINTER_SPEED', 'android.permission.SET_INPUT_CALIBRATION', 'android.permission.SET_KEYBOARD_LAYOUT', 'android.permission.TABLET_MODE', 'android.permission.REQUEST_INSTALL_PACKAGES', 'android.permission.INSTALL_PACKAGES', 'android.permission.CLEAR_APP_USER_DATA', 'android.permission.DELETE_CACHE_FILES', 'android.permission.DELETE_PACKAGES', 'android.permission.MOVE_PACKAGE', 'android.permission.CHANGE_COMPONENT_ENABLED_STATE', 'android.permission.GRANT_RUNTIME_PERMISSIONS', 'android.permission.INSTALL_GRANT_RUNTIME_PERMISSIONS', 'android.permission.REVOKE_RUNTIME_PERMISSIONS', 'android.permission.OBSERVE_GRANT_REVOKE_PERMISSIONS', 'android.permission.ACCESS_SURFACE_FLINGER', 'android.permission.READ_FRAME_BUFFER', 'android.permission.ACCESS_INPUT_FLINGER', 'android.permission.CONFIGURE_WIFI_DISPLAY', 'android.permission.CONTROL_WIFI_DISPLAY', 'android.permission.CONFIGURE_DISPLAY_COLOR_TRANSFORM', 'android.permission.CONTROL_VPN', 'android.permission.CAPTURE_AUDIO_OUTPUT', 'android.permission.CAPTURE_AUDIO_HOTWORD', 'android.permission.MODIFY_AUDIO_ROUTING', 'android.permission.CAPTURE_VIDEO_OUTPUT', 'android.permission.CAPTURE_SECURE_VIDEO_OUTPUT', 'android.permission.MEDIA_CONTENT_CONTROL', 'android.permission.BRICK', 'android.permission.REBOOT', 'android.permission.DEVICE_POWER', 'android.permission.USER_ACTIVITY', 'android.permission.NET_TUNNELING', 'android.permission.FACTORY_TEST', 'android.permission.BROADCAST_PACKAGE_REMOVED', 'android.permission.BROADCAST_SMS', 'android.permission.BROADCAST_WAP_PUSH', 'android.permission.BROADCAST_NETWORK_PRIVILEGED', 'android.permission.MASTER_CLEAR', 'android.permission.CALL_PRIVILEGED', 'android.permission.PERFORM_CDMA_PROVISIONING', 'android.permission.PERFORM_SIM_ACTIVATION', 'android.permission.CONTROL_LOCATION_UPDATES', 'android.permission.ACCESS_CHECKIN_PROPERTIES', 'android.permission.PACKAGE_USAGE_STATS', 'android.permission.CHANGE_APP_IDLE_STATE', 'android.permission.CHANGE_DEVICE_IDLE_TEMP_WHITELIST', 'android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS', 'android.permission.BATTERY_STATS', 'android.permission.BACKUP', 'android.permission.CONFIRM_FULL_BACKUP', 'android.permission.BIND_REMOTEVIEWS', 'android.permission.BIND_APPWIDGET', 'android.permission.BIND_KEYGUARD_APPWIDGET', 'android.permission.MODIFY_APPWIDGET_BIND_PERMISSIONS', 'android.permission.CHANGE_BACKGROUND_DATA_SETTING', 'android.permission.GLOBAL_SEARCH', 'android.permission.GLOBAL_SEARCH_CONTROL', 'android.permission.READ_SEARCH_INDEXABLES', 'android.permission.SET_WALLPAPER_COMPONENT', 'android.permission.READ_DREAM_STATE', 'android.permission.WRITE_DREAM_STATE', 'android.permission.ACCESS_CACHE_FILESYSTEM', 'android.permission.COPY_PROTECTED_DATA', 'android.permission.CRYPT_KEEPER', 'android.permission.READ_NETWORK_USAGE_HISTORY', 'android.permission.MANAGE_NETWORK_POLICY', 'android.permission.MODIFY_NETWORK_ACCOUNTING', 'android.permission.C2D_MESSAGE', 'android.permission.PACKAGE_VERIFICATION_AGENT', 'android.permission.BIND_PACKAGE_VERIFIER', 'android.permission.INTENT_FILTER_VERIFICATION_AGENT', 'android.permission.BIND_INTENT_FILTER_VERIFIER', 'android.permission.SERIAL_PORT', 'android.permission.ACCESS_CONTENT_PROVIDERS_EXTERNALLY', 'android.permission.UPDATE_LOCK', 'android.permission.ACCESS_NOTIFICATIONS', 'android.permission.ACCESS_NOTIFICATION_POLICY', 'android.permission.ACCESS_KEYGUARD_SECURE_STORAGE', 'android.permission.MANAGE_FINGERPRINT', 'android.permission.RESET_FINGERPRINT_LOCKOUT', 'android.permission.CONTROL_KEYGUARD', 'android.permission.TRUST_LISTENER', 'android.permission.PROVIDE_TRUST_AGENT', 'android.permission.LAUNCH_TRUST_AGENT_SETTINGS', 'android.permission.BIND_TRUST_AGENT', 'android.permission.BIND_NOTIFICATION_LISTENER_SERVICE', 'android.permission.BIND_CHOOSER_TARGET_SERVICE', 'android.permission.BIND_CONDITION_PROVIDER_SERVICE', 'android.permission.BIND_DREAM_SERVICE', 'android.permission.INVOKE_CARRIER_SETUP', 'android.permission.ACCESS_NETWORK_CONDITIONS', 'android.permission.ACCESS_DRM_CERTIFICATES', 'android.permission.MANAGE_MEDIA_PROJECTION', 'android.permission.READ_INSTALL_SESSIONS', 'android.permission.REMOVE_DRM_CERTIFICATES', 'android.permission.BIND_CARRIER_MESSAGING_SERVICE', 'android.permission.ACCESS_VOICE_INTERACTION_SERVICE', 'android.permission.BIND_CARRIER_SERVICES', 'android.permission.QUERY_DO_NOT_ASK_CREDENTIALS_ON_BOOT', 'android.permission.KILL_UID', 'android.permission.LOCAL_MAC_ADDRESS', 'android.permission.PEERS_MAC_ADDRESS', 'android.permission.DISPATCH_NFC_MESSAGE']

import requests
import sys
from pprint import pprint
import json

from config import *
from googleplay import GooglePlayAPI
from helpers import sizeof_fmt, print_header_line, print_result_line
from google.protobuf import text_format
from requests.packages.urllib3.exceptions import InsecureRequestWarning

if (len(sys.argv) < 2):
     print "\nUsage: %s appPackageName." % sys.argv[0]
     print "Retrieves the details (i.e. description, URL to screenshots etc) of a specific app.\n"
     sys.exit(0)

# Dealing with user's parameter
appname = sys.argv[1]

# Ignore unverified HTTPS request warning.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

item = {}
try:
     # authentication
     api = GooglePlayAPI(ANDROID_ID)
     api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)

     #invoking api method to get the app details.
     detailsResponse = api.details(appname)

     doc = detailsResponse.docV2

     # if the length of the offer is 0, it means no app is found
     # with the given package name: setting return code to not found (2)
     if not len(doc.offer) > 0:
          item['return_code'] = 2
          print json.dumps(item)
          exit()

     item['micros'] = doc.offer[0].micros
     item['offerType'] = doc.offer[0].offerType
     item['vercode'] = doc.details.appDetails.versionCode
     item['pkg_name'] = doc.details.appDetails.packageName
     item['Details'] = {}
     item['Details']['Description'] = doc.descriptionHtml
     permission_list = doc.details.appDetails.permission
     android_permissions = []
     for p in permission_list:
          if p in VALID_PERMISSIONS:
               android_permissions.append(p)
     #item['Details']['Permissions'] = ','.join(android_permissions)
     item['return_code'] = 1

     print json.dumps(item)

except Exception as e:
     item['return_code'] = 0
     print json.dumps(item)
     
# print text_format.MessageToString(detailsResponse)


