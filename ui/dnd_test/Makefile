TARGET = dnd
SRC_PATH := $(wildcard *.cpp)
INC = -L.
VPATH = . src1 src2

CXXFLAGS += $(shell wx-config --cflags)
LDFLAGS += $(shell wx-config --libs)

CXX=g++
CXXFLAGS += -g

OBJ_DIR =./obj

OBJ_PATH = $(addprefix $(OBJ_DIR)/,$(subst :, ,$(VPATH)))

MAKE_OBJECT_DIR := $(shell mkdir -p $(OBJ_DIR) $(OBJ_PATH))

OBJS = $(addprefix $(OBJ_DIR)/,$(subst .cpp,.o,$(SRC_PATH)))


$(TARGET) : $(OBJS)
	$(CXX) -o $@ $(OBJS) $(INC) $(LDFLAGS)

#$(OBJ_DIR)/%.o : %.cpp %.cpp.d
$(OBJ_DIR)/%.o : %.cpp
	$(CXX) -o $@ -c $< $(INC) $(CXXFLAGS)

.PHONY:clean
clean:
	@rm -rf ./obj
	@rm -rf $(TARGET)
