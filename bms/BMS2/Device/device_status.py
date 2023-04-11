from Device.models import Bms_device_information
import json,threading

def getDeviceStatus():
    data = Bms_device_information.objects.all()
    print(data)
    # d_list = []
    # for i in data:
    #     d = Bms_device_information.objects.get(pk=int(i.pk))
    #     device_info = json.dumps(d.device_informations)

    #     d_list.append({
    #         "record_id":d.pk,
    #         "device_name":d.device_name,
    #         "device_id": device_info["device_id"] if "device_id" in  device_info else None,
    #         "channel_id":device_info["channel_id"] if "channel_id" in device_info else None,
    #         "device_status": device_info["device_status"] if "channel_id" in device_info else None,
    #     })
    
    # return d_list
    
