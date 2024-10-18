import React from 'react';
import './AttendanceForm.css'; // 使用普通 CSS 文件

const AttendanceForm = ({ customerData, handleChange }) => {
  return (
    <div className="attendance-form-container">
      <h2 className="section-title">出勤及反馈</h2>

      <div className="form-group">
        <label className="checkbox-label">
          <input
            type="checkbox"
            name="is_course_reminder"
            checked={customerData.is_course_reminder}
            onChange={handleChange}
          />
          是否到课提醒
        </label>
      </div>

      <div className="form-group">
        <label className="checkbox-label">
          <input
            type="checkbox"
            name="attended_first_live"
            checked={customerData.attended_first_live}
            onChange={handleChange}
          />
          参加第一天直播
        </label>
      </div>

      <div className="form-group">
        <label>第一天观看时间 (分钟):</label>
        <input
          type="number"
          className="form-control"
          name="first_day_watch_duration"
          value={customerData.first_day_watch_duration}
          onChange={handleChange}
          placeholder="输入分钟数"
        />
      </div>

      <div className="form-group">
        <label className="checkbox-label">
          <input
            type="checkbox"
            name="attended_second_live"
            checked={customerData.attended_second_live}
            onChange={handleChange}
          />
          参加第二天直播
        </label>
      </div>

      <div className="form-group">
        <label>第二天观看时间 (分钟):</label>
        <input
          type="number"
          className="form-control"
          name="second_day_watch_duration"
          value={customerData.second_day_watch_duration}
          onChange={handleChange}
          placeholder="输入分钟数"
        />
      </div>

      <div className="form-group">
        <label className="checkbox-label">
          <input
            type="checkbox"
            name="additional_students"
            checked={customerData.additional_students}
            onChange={handleChange}
          />
          马甲加学员
        </label>
      </div>

      <div className="form-group">
        <label className="checkbox-label">
          <input
            type="checkbox"
            name="comments_count"
            checked={customerData.comments_count}
            onChange={handleChange}
          />
          评论数
        </label>
      </div>

      <div className="form-group">
        <label className="checkbox-label">
          <input
            type="checkbox"
            name="persona_chat"
            checked={customerData.persona_chat}
            onChange={handleChange}
          />
          是否进行人设聊天
        </label>
      </div>

      <div className="form-group">
        <label>第一天观后反馈:</label>
        <select
          className="form-control"
          name="first_day_feedback"
          value={customerData.first_day_feedback}
          onChange={handleChange}
        >
          <option value="满意">满意</option>
          <option value="一般">一般</option>
          <option value="不考虑">不考虑</option>
        </select>
      </div>

      <div className="form-group">
        <label>第二天观后反馈:</label>
        <select
          className="form-control"
          name="second_day_feedback"
          value={customerData.second_day_feedback}
          onChange={handleChange}
        >
          <option value="满意">满意</option>
          <option value="一般">一般</option>
          <option value="不考虑">不考虑</option>
        </select>
      </div>

      <div className="form-group">
        <label>客户其他描述:</label>
        <textarea
          className="form-control"
          name="description"
          value={customerData.description}
          onChange={handleChange}
          rows="3"
          placeholder="请输入客户描述"
          required
        />
      </div>
    </div>
  );
};

export default AttendanceForm;