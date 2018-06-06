
def positions_interpolate(p_left, t_left, p_right, t_right, times):
  times_scaled = (times - t_left) / (t_right - t_left)
  return [p_left + time * (p_right - p_left) for time in times_scaled]
