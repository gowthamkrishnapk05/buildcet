import cv2 as cv
import numpy as np
height = 500
width = 950
gnd = 370
obstacle_width = 40
obstacle_height = 60
ball_radius = 20
ball_position = 150
obstacle_pos = width
score=0
game_over = False

ball_y = gnd-ball_radius
velocity = 0
gravity = 2
is_jump = False
speed = 10

while True:

    img = np.ones((height,width,3),dtype=np.uint8)*255
    cv.line(img,(0,gnd),(width,gnd),(0,0,0),2)

    if not game_over:
        key = cv.waitKey(30) & 0xff

        if key == 32 and ball_y == gnd-ball_radius:
            velocity = -23
            is_jump = True

        if key == ord('q'):
            break

        velocity += gravity
        ball_y += velocity

        if ball_y >= (gnd-ball_radius):
            ball_y = (gnd-ball_radius)
            velocity=0
            is_jump = False

        obstacle_pos -= speed
        if obstacle_pos < 0:
            obstacle_pos = width
            score+=1

        if (obstacle_pos < ball_position + ball_radius) and (obstacle_pos + obstacle_width > ball_position - ball_radius):
            if ball_y + ball_radius >= gnd - obstacle_height:
                game_over = True
    
    cv.circle(img, (ball_position, int(ball_y)), ball_radius, (0, 0, 255), -1)    

    pt1 = (int(obstacle_pos), gnd - obstacle_height)
    pt2 = (int(obstacle_pos + obstacle_width), gnd)
    cv.rectangle(img, pt1, pt2, (100, 100, 100), -1)       

    cv.putText(img, f"Score: {score}", (width - 200, 50), 
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    
    if game_over:
        cv.putText(img, "GAME OVER", (width//2 - 150, height//2), 
                   cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        cv.putText(img, "Press 'r' to Restart or 'q' to Quit", (width//2 - 200, height//2 + 50), 
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    

        cv.imshow("ball",img)
        key = cv.waitKey(0) & 0xff
        if key == ord('r'):
            game_over = False
            score = 0
            obstacle_pos = width
            ball_y = gnd-ball_radius
            velocity = 0
        elif key == ord('q'):
                    break
    else:
        cv.imshow("ball", img)
cv.destroyAllWindows()
