import librosa
import numpy as np
import matplotlib.pyplot as plt

def extract_pitch(audio_file, start_time=0, end_time=3.36, num_points=10):
    y, sr = librosa.load(audio_file, sr=16000)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    f0_librosa = []
    for t in range(pitches.shape[1]):
        index = magnitudes[:, t].argmax()
        pitch = pitches[index, t]
        f0_librosa.append(pitch if pitch > 0 else np.nan)
    f0, voiced_flag, voiced_probs = librosa.pyin(y=y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
    print(f0[39])

    start_sample = int(start_time * sr)
    end_sample = int(end_time * sr)
    step = (end_sample - start_sample) // num_points

    average_pitches = []
    for i in range(num_points):
        sample_range = pitches[start_sample + i * step:start_sample + (i + 1) * step]
        average_pitch = np.mean(sample_range[sample_range != 0])
        average_pitches.append(average_pitch)

    return average_pitches

audio_file = r''
result = extract_pitch(audio_file)
print(result)


# 加载音频文件
audio_path = r''  # 替换为你的音频文件路径
y, sr = librosa.load(audio_path, sr=None)  # sr=None 表示使用原始采样率

# 指定你想要提取基频的音频段落
start_time = 1.11  # 开始时间，单位为秒
end_time = 1.36    # 结束时间，单位为秒

# 计算该段落的起始和结束索引
start_sample = int(start_time * sr)
end_sample = int(end_time * sr)

# 提取指定段落的音频
y_segment = y[start_sample:end_sample]

# 使用pyptrack追踪基频
y_harmonics, pitches = librosa.piptrack(y=y_segment, sr=sr)

# 计算10个平均位置的基频
# 首先，找到10个平均位置的索引
num_average_positions = 10
average_positions = np.linspace(start_sample, end_sample, num_average_positions, dtype=int)

# 初始化一个列表来存储这些位置的基频
average_pitches = []

for pos in average_positions:
    # 计算该位置的基频
    pitch_at_pos = pitches[pos // sr]  # 由于pitches是按时间序列提供的，需要将其转换为对应的索引
    average_pitches.append(pitch_at_pos)

# 计算平均基频
average_pitch = np.mean(average_pitches)

# 打印结果
print(f"10个平均位置的平均基频（Hz）: {average_pitch}")

# 绘制基频变化曲线
plt.figure(figsize=(10, 4))
times = librosa.times_like(pitches)
plt.plot(times, pitches, label='Pitch')
plt.axvline(x=start_time, color='r', linestyle='--', label=f'Start time: {start_time}s')
plt.axvline(x=end_time, color='g', linestyle='--', label=f'End time: {end_time}s')
plt.legend()
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency (Hz)')
plt.title('Pitch over time')
plt.show()

# import librosa
# import numpy as np
# import matplotlib.pyplot as plt

# # 加载音频文件
# audio_path = 'path_to_your_audio_file.wav'  # 替换为你的音频文件路径
# y, sr = librosa.load(audio_path, sr=None)  # sr=None 表示使用原始采样率

# # 指定你想要提取共振峰的音频段落
# start_time = 10  # 开始时间，单位为秒
# end_time = 20    # 结束时间，单位为秒

# # 计算该段落的起始和结束索引
# start_sample = int(start_time * sr)
# end_sample = int(end_time * sr)

# # 提取指定段落的音频
# y_segment = y[start_sample:end_sample]

# # 计算该段落的线性预测编码（LPC）系数
# lpc_order = 2 + int(sr / 1000)  # LPC阶数，通常为采样率的1/1000到1/500
# lpc_coeffs = librosa.lpc(y_segment, lpc_order)

# # 计算共振峰频率
# # 从LPC系数中提取共振峰频率
# # 这里使用一个简化的方法，即找到LPC多项式的根
# # 注意：这种方法可能不适用于所有类型的音频
# roots = np.roots(lpc_coeffs)
# frequencies = np.abs(roots)  # 共振峰频率

# # 过滤掉高频部分，只保留共振峰频率
# # 假设共振峰频率不会超过5000Hz
# formant_frequencies = frequencies[frequencies <= 5000]

# # 打印共振峰频率
# print("共振峰频率（Hz）:", formant_frequencies)

# # 绘制共振峰频率
# plt.figure(figsize=(10, 4))
# plt.stem(formant_frequencies, use_line_collection=True)
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')
# plt.title('Formant Frequencies')
# plt.show()