import base64
import json
import sys

secret_string_cn = "W3sib2F1dGhfdG9rZW4iOiAiZmJiZTBiOWUtY2I2Ni00YjU1LTgyM2QtMTE4YWE0ZDdmODM5IiwgIm9hdXRoX3Rva2VuX3NlY3JldCI6ICJWTDJheVVVMTNlVXJ3bmw3RElZeVdUdDNmRmFzSURWVndqbCIsICJtZmFfdG9rZW4iOiBudWxsLCAibWZhX2V4cGlyYXRpb25fdGltZXN0YW1wIjogbnVsbCwgImRvbWFpbiI6ICJnYXJtaW4uY24ifSwgeyJzY29wZSI6ICJDT01NVU5JVFlfQ09VUlNFX1JFQUQgR0FSTUlOUEFZX1dSSVRFIEdPTEZfQVBJX1JFQUQgQVRQX1JFQUQgR0hTX1NBTUQgR0hTX1VQTE9BRCBJTlNJR0hUU19SRUFEIENPTU1VTklUWV9DT1VSU0VfV1JJVEUgQ09OTkVDVF9XUklURSBHQ09GRkVSX1dSSVRFIEdBUk1JTlBBWV9SRUFEIERUX0NMSUVOVF9BTkFMWVRJQ1NfV1JJVEUgR09MRl9BUElfV1JJVEUgSU5TSUdIVFNfV1JJVEUgUFJPRFVDVF9TRUFSQ0hfUkVBRCBPTVRfQ0FNUEFJR05fUkVBRCBPTVRfU1VCU0NSSVBUSU9OX1JFQUQgR0NPRkZFUl9SRUFEIENPTk5FQ1RfUkVBRCBBVFBfV1JJVEUiLCAianRpIjogIjM2N2RiMWRiLTMzYTQtNGQ0OC04MWUyLWIyNTAwOGJkMWVhMyIsICJ0b2tlbl90eXBlIjogIkJlYXJlciIsICJhY2Nlc3NfdG9rZW4iOiAiZXlKaGJHY2lPaUpTVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0lzSW10cFpDSTZJbVJwTFc5aGRYUm9MWE5wWjI1bGNpMXdjbTlrTFdOdU1TMHlNREkwTFhFeEluMC5leUp6WTI5d1pTSTZXeUpCVkZCZlVrVkJSQ0lzSWtGVVVGOVhVa2xVUlNJc0lrTlBUVTFWVGtsVVdWOURUMVZTVTBWZlVrVkJSQ0lzSWtOUFRVMVZUa2xVV1Y5RFQxVlNVMFZmVjFKSlZFVWlMQ0pEVDA1T1JVTlVYMUpGUVVRaUxDSkRUMDVPUlVOVVgxZFNTVlJGSWl3aVJGUmZRMHhKUlU1VVgwRk9RVXhaVkVsRFUxOVhVa2xVUlNJc0lrZEJVazFKVGxCQldWOVNSVUZFSWl3aVIwRlNUVWxPVUVGWlgxZFNTVlJGSWl3aVIwTlBSa1pGVWw5U1JVRkVJaXdpUjBOUFJrWkZVbDlYVWtsVVJTSXNJa2RJVTE5VFFVMUVJaXdpUjBoVFgxVlFURTlCUkNJc0lrZFBURVpmUVZCSlgxSkZRVVFpTENKSFQweEdYMEZRU1Y5WFVrbFVSU0lzSWtsT1UwbEhTRlJUWDFKRlFVUWlMQ0pKVGxOSlIwaFVVMTlYVWtsVVJTSXNJazlOVkY5RFFVMVFRVWxIVGw5U1JVRkVJaXdpVDAxVVgxTlZRbE5EVWtsUVZFbFBUbDlTUlVGRUlpd2lVRkpQUkZWRFZGOVRSVUZTUTBoZlVrVkJSQ0pkTENKcGMzTWlPaUpvZEhSd2N6b3ZMMlJwWVhWMGFDNW5ZWEp0YVc0dVkyNGlMQ0p5WlhadlkyRjBhVzl1WDJWc2FXZHBZbWxzYVhSNUlqcGJJa2RNVDBKQlRGOVRTVWRPVDFWVUlsMHNJbU5zYVdWdWRGOTBlWEJsSWpvaVZVNUVSVVpKVGtWRUlpd2laWGh3SWpveE56TXhNRFl6T0RjNUxDSnBZWFFpT2pFM016QTVOelU0Tnprc0ltZGhjbTFwYmw5bmRXbGtJam9pT0RrMU56TXpPVFF0T0ROa01DMDBPRFkyTFdJNU1tVXRObVV5TXpFMk1HVTNZV1V6SWl3aWFuUnBJam9pTXpZM1pHSXhaR0l0TXpOaE5DMDBaRFE0TFRneFpUSXRZakkxTURBNFltUXhaV0V6SWl3aVkyeHBaVzUwWDJsa0lqb2lSMEZTVFVsT1gwTlBUazVGUTFS"

secret_string_cn = secret_string_cn.strip()  # 去除可能的换行或空格

# 如果长度不是 4 的倍数，补充 `=` 填充符
while len(secret_string_cn) % 4 != 0:
    secret_string_cn += '='


try:
    decoded_string = base64.b64decode(secret_string_cn)
    print("Decoded CN Secret String:", decoded_string)
    json.loads(decoded_string)
except Exception as e:
    print("Error decoding secret_string_cn:", e)
    sys.exit(1)