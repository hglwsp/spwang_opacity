function [] = FcnRemoveWhiteSpace(Hgcf,Axes)
%***********************************************************************
%函数说明：通过调整figure中座标轴大小和位置，消除figure的空白区域最小
%参数：   Hgcf   图片figure的句柄
%         Axes   图片中各子图subplot的座标轴句柄，为Nrow*Ncol维的结构体矩阵阵
%                Axes(i,j)代表第i行，第j列的座标轴对象
% bug: 2020-04-10
% can not draw with non complete subplot---posotion is not correct.
%***********************************************************************

% Example
% Hgcf=figure('color','w');
% x = 1:4;
% y = [5000:5003;50:53;5000:5003;...
%      5:8;5000000:5000003;5:8;...
%      5000:5003;50:53;5:8;];
%
%  nrow=3; ncol = 3;
% for i=1:9
%     subplot(nrow,ncol,i)
%     plot(x,y(i,:));
%     ylabel(['X',num2str(i)]);
%     xlabel('t(s)');
%     AX(i)=gca;
% end
%
% AX = reshape(AX,[ncol,nrow])';
% drawnow
% graph.FcnRemoveWhiteSpace(Hgcf,AX);

%--------------自动获得subplot的行列数------------------------
Dimensions=size(Axes);
Nrow=Dimensions(1);
Ncol=Dimensions(2);
%------------为避免最后图片显得太过拥挤，设置四周留白大小百分比------
WhiteSpaceLeftRatio=0.1;         %设置四周空白区域留下10%不去除
Ratio=1-WhiteSpaceLeftRatio;
%----------获得每个座标轴的TightInset的位置向量---------
for i=1:Nrow
    for j=1:Ncol
        if Axes(i,j).isprop('Position')
            left=Axes(i,j).Position(1)-Axes(i,j).TightInset(1);
            bottom=Axes(i,j).Position(2)-Axes(i,j).TightInset(2);
            width=Axes(i,j).Position(3)+Axes(i,j).TightInset(1)+Axes(i,j).TightInset(3);
            height=Axes(i,j).Position(4)+Axes(i,j).TightInset(2)+Axes(i,j).TightInset(4);
            AxesTightInsetPosition(i,j).TightInsetPosition=[left bottom width height];
        end
    end
end
%-------计算图片四周的空白区域，获得需要填满的空白区域的宽度和高度----

%求最左边空白
temp = 1000; % temp=AxesTightInsetPosition(1,1).TightInsetPosition(1);
for i=1:Nrow
    if Axes(i,1).isprop('Position')
        temp=min(temp,AxesTightInsetPosition(i,1).TightInsetPosition(1));
    end
end
WhiteLeft=temp;

%求最下边空白
temp = 1000; %temp=AxesTightInsetPosition(Nrow,1).TightInsetPosition(2);
for j=1:Ncol
    if Axes(Nrow,j).isprop('Position')
        temp=min(temp,AxesTightInsetPosition(Nrow,j).TightInsetPosition(2));
    end
end
WhiteBottom=temp;

%求最右边空白   %temp=AxesTightInsetPosition(1,Ncol).TightInsetPosition(1)+AxesTightInsetPosition(1,Ncol).TightInsetPosition(3);
for i=1:Nrow
    if Axes(i,Ncol).isprop('Position')
        temp=max(temp,AxesTightInsetPosition(i,Ncol).TightInsetPosition(1)+AxesTightInsetPosition(i,Ncol).TightInsetPosition(3));
    end
end
WhiteRight=1-temp;

%求最上边空白     %temp=AxesTightInsetPosition(1,1).TightInsetPosition(2)+AxesTightInsetPosition(1,1).TightInsetPosition(4);
for j=1:Ncol
    if Axes(1,j).isprop('Position')
        temp=max(temp,AxesTightInsetPosition(1,j).TightInsetPosition(2)+AxesTightInsetPosition(1,j).TightInsetPosition(4));
    end
end
WhiteTop=1-temp;

%求总的空白，并平均分配到每个座标轴的高度和宽度增量
WhiteWidth=WhiteLeft+WhiteRight;
WhiteHeight=WhiteBottom+WhiteTop;
deltaW=WhiteWidth/Ncol*Ratio;
deltaH=WhiteHeight/Nrow*Ratio;

%----------调整座标轴的位置和宽度高度，使空白区域被填满------------
%调整每个座标轴的宽度和高度
for i=1:Nrow
    for j=1:Ncol
        if Axes(i,j).isprop('Position')
            Axes(i,j).Position(3)=Axes(i,j).Position(3)+deltaW;
            Axes(i,j).Position(4)=Axes(i,j).Position(4)+deltaH;
        end
    end
end

%调整每个座标轴的水平位置
for i=1:Nrow
    for j=1:Ncol
        if Axes(i,j).isprop('Position')
            if(j==1)   %第一列：往左移动WhiteLeft
                Axes(i,j).Position(1)=Axes(i,j).Position(1)-WhiteLeft*Ratio;
            else      %其他列
                Axes(i,j).Position(1)=Axes(i,j).Position(1)-WhiteLeft*Ratio+(j-1)*deltaW;
            end
        end
    end
end
%调整每个座标轴的垂直位置
for i=Nrow:-1:1
    for j=1:Ncol
        if Axes(i,j).isprop('Position')
            if(i==Nrow)    %最后一行：往下移动WhiteBottom
                Axes(i,j).Position(2)=Axes(i,j).Position(2)-WhiteBottom*Ratio;
            else         %其他行
                Axes(i,j).Position(2)=Axes(i,j).Position(2)-WhiteBottom*Ratio+(Nrow-i)*deltaH;
            end
        end
    end
end