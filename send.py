
import paho.mqtt.publish as publish

publish.single("Ucc/Jaycute", "There's a clocktower from Hereforth where the names of the dead are inscribed. Their memories are all that's left when the bastards have taken everything else. We hold on to their good deeds even as their faces fade from our memories.", hostname="104.248.163.70", port=1883)

