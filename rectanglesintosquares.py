def sqInRect(lng, wdth):
	if lng = wdth:
		return None
	result = []
	while lng != wdth:
		if lng > wdth:
			lng = lng - wdth
			result.append(wdth)
		if wdth > lng:
			wdth = wdth - lng
			result.append(lng)
	result.append(lng)
	return result
