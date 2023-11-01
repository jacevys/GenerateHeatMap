import numpy as np
import matplotlib.pyplot as plt
#
def gmp(height, width, coordinate_set, hm_ratio):
	radius = int(min(height, width) * hm_ratio)
	w_0 = 1
	hm_range = 5

	for index, coordinate in enumerate(coordinate_set):
		canvas = np.zeros((height + 2 * radius, width + 2 * radius))
		x = np.linspace(-hm_range, hm_range, radius)
		y = np.linspace(-hm_range, hm_range, radius)
		xx, yy = np.meshgrid(x, y)

		gaussian_distribution = np.exp(-((pow(xx, 2) + pow(yy, 2)) / pow(w_0, 2)))
		canvas[int(coordinate[0] + radius - 0.5 * radius):int(coordinate[0] + radius + 0.5 * radius), int(coordinate[1] + radius - 0.5 * radius):int(coordinate[1] + radius + 0.5 * radius)] = gaussian_distribution
		canvas = canvas[radius:height + radius, radius:width + radius]
		canvas = np.expand_dims(canvas, axis=-1)

		if index == 0:
			heatmap = canvas
		else:
			heatmap = np.concatenate([heatmap, canvas], axis=-1)

	return heatmap
#
def displayHeatMap(heatmap):
	figure = plt.figure(figsize=(8, 6))

	for index in range(heatmap.shape[-1]):
		plt.subplot(heatmap.shape[-1], 1, (index + 1))
		plt.imshow(heatmap[:, :, index])
		plt.axis('off')

	plt.show()
#
def main():
	coordinate_set = [[1080, 50], [500, 500], [300, 1000]]
	heatmap = gmp(1088, 2048, coordinate_set, 0.5)
	displayHeatMap(heatmap)
#
if __name__ == '__main__':
	main()